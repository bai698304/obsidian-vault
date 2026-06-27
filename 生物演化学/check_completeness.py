"""
鬼谷说下载完整性预检
扫描 Download 目录，对比视频列表，报告哪些已下载、哪些缺失

用法:
  python check_completeness.py                     # 完整报告
  python check_completeness.py --quiet             # 仅输出数字
  python check_completeness.py --missing-only       # 仅列出缺失项
"""
import json
import sys
from difflib import SequenceMatcher
from pathlib import Path

BASE = Path(r"D:\obsidian\vault\生物演化学")
DOWNLOAD_DIR = Path(r"D:\jijidown(Bilibili video download tool)\Download")
JSON_PATH = BASE / "_video_list.json"

AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".flac", ".ogg", ".opus", ".aac", ".wma"}


def find_audio_files():
    """扫描 Download 目录下所有音频文件"""
    if not DOWNLOAD_DIR.exists():
        return []
    files = []
    for ext in AUDIO_EXTS:
        files.extend(DOWNLOAD_DIR.rglob(f"*{ext}"))
        files.extend(DOWNLOAD_DIR.rglob(f"*{ext.upper()}"))
    # 去重
    seen = set()
    unique = []
    for f in sorted(files):
        if f.name.lower() not in seen:
            seen.add(f.name.lower())
            unique.append(f)
    return unique


def match_audio_to_video(audio_files: list, videos: list) -> dict:
    """为每个音频文件找到最佳匹配的视频条目，返回 {video_index: audio_file}"""
    matched = {}  # video_index -> audio_file
    used_audio = set()  # 已匹配的音频文件，防止一文件匹配多视频

    for v_idx, v in enumerate(videos):
        title = v["title"]
        safe = v["safe_filename"]
        bv = v["bv"]

        best_score = 0.0
        best_audio = None

        for af in audio_files:
            if af.name.lower() in used_audio:
                continue  # 已匹配给其他视频，跳过
            af_name = af.stem.lower()

            # 策略1: BV号精确匹配
            if bv.lower() in af_name:
                best_audio = af
                best_score = 1.0
                break

            # 策略2: 视频标题作为子串出现在文件名中 (jiidown 命名格式)
            # jiidown 文件命名: "【鬼谷说】标题 - 1.xxx.h265(AvXXX).mp3"
            if title.lower() in af_name:
                best_audio = af
                best_score = 0.99
                break

            # 策略3: 安全文件名子串匹配
            safe_stem = Path(safe).stem.lower()
            if safe_stem in af_name:
                best_audio = af
                best_score = 0.95
                break

            # 策略4: SequenceMatcher 模糊匹配 (兜底)
            score4 = SequenceMatcher(None, af_name, safe_stem).ratio()
            if score4 > best_score:
                best_score = score4
                best_audio = af

            score5 = SequenceMatcher(None, af_name, title.lower()).ratio()
            if score5 > best_score:
                best_score = score5
                best_audio = af

        if best_score >= 0.3 and best_audio:
            matched[v_idx] = best_audio
            used_audio.add(best_audio.name.lower())

    return matched


def main():
    quiet = "--quiet" in sys.argv
    missing_only = "--missing-only" in sys.argv

    if not JSON_PATH.exists():
        print(f"[ERROR] Video list not found: {JSON_PATH}")
        sys.exit(1)

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        videos = json.load(f)

    audio_files = find_audio_files()
    matched = match_audio_to_video(audio_files, videos)

    found_count = len(matched)
    total = len(videos)
    missing = total - found_count

    if quiet:
        print(f"{found_count}/{total}")
        sys.exit(0 if found_count == total else 1)

    # 完整报告
    print("=" * 60)
    print("  鬼谷说下载完整性检查")
    print("=" * 60)
    print(f"\n  总计: {total} 期")
    print(f"  已下载: {found_count} 期")
    print(f"  缺失: {missing} 期")
    pct = found_count * 100 // total
    bar = "[" + "#" * (pct // 5) + "." * (20 - pct // 5) + "]"
    print(f"  进度: {bar} {pct}%")

    if not missing_only:
        print(f"\n{'-' * 60}")
        print("  已下载列表:")
        print(f"{'-' * 60}")
        for v_idx, af in sorted(matched.items()):
            v = videos[v_idx]
            print(f"  [OK] {v['dir']}/ {v['title']}")
            print(f"       file: {af.name}")

    if missing > 0:
        print(f"\n{'-' * 60}")
        print(f"  缺失列表 ({missing} 期):")
        print(f"{'-' * 60}")
        missing_indices = set(range(total)) - set(matched.keys())
        for v_idx in sorted(missing_indices):
            v = videos[v_idx]
            print(f"  [MISS] {v['dir']}/")
            print(f"         {v['title']}")
            print(f"         {v['bv']}  ->  https://www.bilibili.com/video/{v['bv']}")

    # 兜底: 存在但无法匹配的音频文件
    matched_filenames = {af.name.lower() for af in matched.values()}
    unmatched_audio = [af for af in audio_files if af.name.lower() not in matched_filenames]
    if unmatched_audio and not missing_only:
        print(f"\n{'-' * 60}")
        print(f"  无法匹配的音频文件 ({len(unmatched_audio)}):")
        print(f"{'-' * 60}")
        for af in unmatched_audio:
            print(f"  [?] {af.name}")

    print()

    if found_count == total:
        print("[READY] 全部 60 期已就绪，可以开始转录。")
    else:
        print(f"[PARTIAL] 还差 {missing} 期，可以分批转录或继续下载。")


if __name__ == "__main__":
    main()
