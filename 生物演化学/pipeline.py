"""
鬼谷说转录后处理管道
将 FunASR 输出的 txt 转录文本匹配并插入到 Obsidian markdown 文件中

用法:
  1. 先用 jiidown 下载所有视频为 mp3，放到 Download 目录
  2. 运行 FunASR 批量转写:
     D:\funasr_project\run.bat "D:\jijidown(Bilibili video download tool)\Download\"
  3. 运行本脚本完成最后一步:
     python D:\obsidian\vault\生物演化学\pipeline.py

也可手动指定输入目录:
  python pipeline.py --input "D:\some\folder\output"
"""
import json
import os
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

# === 配置 ===
BASE = Path(r"D:\obsidian\vault\生物演化学")
VIDEO_LIST = BASE / "_video_list.json"
FUNASR_OUTPUT_DEFAULT = Path(r"D:\jijidown(Bilibili video download tool)\Download\output")


def load_video_list():
    """加载视频列表"""
    with open(VIDEO_LIST, "r", encoding="utf-8") as f:
        return json.load(f)


def strip_prefixes(name: str) -> str:
    """移除常见前缀/后缀，提取核心标题"""
    # 去扩展名
    name = Path(name).stem
    # 去B站前缀
    name = re.sub(r'^【鬼谷说】', '', name)
    name = re.sub(r'^鬼谷说[：:]', '', name)
    # 去可能的多余空格
    name = name.strip()
    return name


def match_score(txt_name: str, video: dict) -> float:
    """计算 txt 文件名与视频条目的匹配分数 (0~1)"""
    txt_clean = strip_prefixes(txt_name).lower()

    # 策略1: BV号精确匹配 (最高优先级)
    bv = video["bv"].lower()
    if bv in txt_name.lower():
        return 1.0

    # 策略2: 视频标题作为子串 (jiidown/FunASR 命名格式)
    title_lower = video["title"].lower()
    if title_lower in txt_clean:
        return 0.99

    # 策略3: 安全文件名子串匹配
    safe = video["safe_filename"].lower()
    safe_stem = Path(safe).stem.lower()
    if safe_stem in txt_clean:
        return 0.95

    # 策略4: SequenceMatcher 模糊匹配 (兜底)
    core_title = strip_prefixes(title_lower)
    score1 = SequenceMatcher(None, txt_clean, core_title).ratio()
    score2 = SequenceMatcher(None, txt_clean, safe_stem).ratio()

    return max(score1, score2)


def find_best_match(txt_path: Path, videos: list) -> dict | None:
    """为 txt 文件找到最佳匹配的视频条目"""
    best_video = None
    best_score = 0.0

    for v in videos:
        score = match_score(txt_path.name, v)
        if score > best_score:
            best_score = score
            best_video = v

    if best_score < 0.5:
        print(f"  [WARN] Low match confidence ({best_score:.2f}): {txt_path.name}")
        return None

    return best_video


def update_markdown(video: dict, transcript: str):
    """将转录文本插入到 Obsidian markdown 文件中"""
    md_path = Path(video["filepath"])

    if not md_path.exists():
        print(f"  [ERROR] Markdown not found: {md_path}")
        return False

    content = md_path.read_text(encoding="utf-8")

    # 替换"待 FunASR 转写后填入"占位符
    placeholder = "*待 FunASR 转写后填入*"
    if placeholder in content:
        content = content.replace(placeholder, transcript)
    else:
        # 如果占位符已被替换过，追加到转录文本段落后
        marker = "## 转录文本\n\n"
        if marker in content:
            # 检查是否已有内容
            after_marker = content.split(marker, 1)[1]
            if after_marker.startswith("*待 FunASR"):
                content = content.replace(
                    marker + placeholder,
                    marker + transcript
                )
            else:
                # 已有内容，在末尾追加分隔符后添加新转录
                content = content.replace(
                    marker + after_marker.split("\n\n---", 1)[0] if "\n\n---" in after_marker else marker + after_marker.split("\n\n##", 1)[0],
                    marker + transcript,
                    1
                )
                print(f"  [INFO] Replaced existing transcript")

    # 更新状态
    content = content.replace("status: pending", "status: active")

    md_path.write_text(content, encoding="utf-8")
    return True


def update_index(videos: list):
    """更新总索引中的状态标记"""
    index_path = BASE / "_鬼谷说总索引.md"
    if not index_path.exists():
        return

    content = index_path.read_text(encoding="utf-8")
    for v in videos:
        md_path = Path(v["filepath"])
        if md_path.exists():
            md_content = md_path.read_text(encoding="utf-8")
            if "status: active" in md_content:
                # 更新索引中的状态
                content = content.replace(
                    f"| {v['title']} | `{v['bv']}` | ⬜ pending |",
                    f"| {v['title']} | `{v['bv']}` | 🔄 active |"
                )

    index_path.write_text(content, encoding="utf-8")


def find_txt_files(input_dir: Path) -> list:
    """递归查找所有 txt 文件"""
    if not input_dir.exists():
        print(f"[ERROR] Directory not found: {input_dir}")
        return []

    txt_files = list(input_dir.rglob("*.txt"))
    return sorted(txt_files)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="鬼谷说转录后处理管道")
    parser.add_argument("--input", "-i", type=str,
                        default=str(FUNASR_OUTPUT_DEFAULT),
                        help=f"FunASR 输出目录 (默认: {FUNASR_OUTPUT_DEFAULT})")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅预览匹配结果，不写入文件")
    args = parser.parse_args()

    input_dir = Path(args.input)

    print("=" * 60)
    print("  鬼谷说转录后处理管道")
    print("=" * 60)

    # 加载视频列表
    videos = load_video_list()
    print(f"\n[LOAD] {len(videos)} videos in database")

    # 查找 txt 文件
    txt_files = find_txt_files(input_dir)
    if not txt_files:
        print(f"\n[ERROR] No .txt files found in: {input_dir}")
        print(f"[HINT] Make sure you've run FunASR first:")
        print(f'  D:\\funasr_project\\run.bat "D:\\jijidown(Bilibili video download tool)\\Download\\"')
        sys.exit(1)

    print(f"[FIND] {len(txt_files)} transcription files in: {input_dir}")
    for t in txt_files:
        print(f"  - {t.name}")

    # 匹配 & 处理
    print(f"\n{'─' * 60}")
    print("  Matching & Updating...")
    print(f"{'─' * 60}")

    matched = 0
    unmatched = []
    updated_videos = []

    for txt_file in txt_files:
        video = find_best_match(txt_file, videos)
        if video is None:
            unmatched.append(txt_file)
            continue

        transcript = txt_file.read_text(encoding="utf-8").strip()
        if not transcript:
            print(f"  [SKIP] Empty transcript: {txt_file.name}")
            continue

        print(f"  [MATCH] {txt_file.name}")
        print(f"       -> {video['title']} (score check OK)")
        print(f"       -> {video['dir']}/{video['safe_filename']}.md")

        if not args.dry_run:
            if update_markdown(video, transcript):
                print(f"       -> [UPDATED] status: pending -> active")
                updated_videos.append(video)
        matched += 1

    # 更新索引
    if updated_videos and not args.dry_run:
        update_index(updated_videos)
        print(f"\n[INDEX] Updated {len(updated_videos)} entries")

    # 报告
    print(f"\n{'=' * 60}")
    print(f"  RESULTS")
    print(f"{'=' * 60}")
    print(f"  Total txt files:   {len(txt_files)}")
    print(f"  Successfully matched: {matched}")
    print(f"  Unmatched:           {len(unmatched)}")

    if unmatched:
        print(f"\n  [UNMATCHED] These files need manual mapping:")
        for u in unmatched:
            print(f"    - {u.name}")
        print(f"\n  Copy the filename and manually find the BV match in _video_list.json")

    if args.dry_run:
        print(f"\n  [DRY RUN] No files were modified. Remove --dry-run to apply.")
    else:
        print(f"\n  Done! Open Obsidian to see the updated notes.")


if __name__ == "__main__":
    main()
