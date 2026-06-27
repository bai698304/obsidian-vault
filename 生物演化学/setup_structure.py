"""
鬼谷说合集 — Obsidian 目录结构生成器
在 D:\obsidian\vault\生物演化学 下创建分类文件夹及 60 期视频的 markdown 骨架
"""
import json
import os
from pathlib import Path

BASE = Path(r"D:\obsidian\vault\生物演化学")

CATEGORIES = [
    {
        "dir": "01_节肢动物",
        "videos": [
            ("奇虾：初代霸主的故事", "BV1wb41127jT"),
            ("三叶虫：一个平凡家族的不屈与彷徨", "BV1jb411H7aa"),
            ("螯肢动物：死生一念 世路茫然", "BV1n441147Wq"),
            ("蜘蛛：结网的三重境界", "BV1Hx4y1n7ts"),
            ("昆虫：被偏爱的都有恃无恐", "BV1X4411P7ce"),
            ("蜚蠊目：飒爽奔跑在演化的夹缝中", "BV1Yg9aB5ELN"),
            ("鳞翅目：等待亿年的邂逅", "BV1614y1a7cs"),
            ("藤壶：那诡寄多端的过往……", "BV1AX4y1J7TU"),
        ]
    },
    {
        "dir": "02_软体动物",
        "videos": [
            ("软体动物（其一）：家里有矿可劲儿浪", "BV1gb411t7DT"),
            ("软体动物（其二）：一场跨越三亿年的秘密战争", "BV1Xb411M7br"),
            ("软体动物（其三）：远古王者的不屈征途", "BV1Sb411G726"),
            ("蛸类：宿命的轮回", "BV1JBFSecE2c"),
            ("菊石（其一）：旧神的涅槃", "BV16B4y1X7ap"),
            ("菊石（其二）：此花开尽更无花", "BV1TY4y157Hi"),
        ]
    },
    {
        "dir": "03_棘皮与腔肠动物",
        "videos": [
            ("棘皮动物：六亲不认的演化步伐", "BV1Nb411h7bc"),
            ("海胆：吾之演化 浑身是胆！", "BV1voZ7BnEF1"),
            ("水母：原初与彼方的超然魅影", "BV1v4411L7Ee"),
        ]
    },
    {
        "dir": "04_海绵与蠕虫",
        "videos": [
            ("海绵：轮回引渡人", "BV1Qh411E7LL"),
            ("古蠕虫：历史的车辙", "BV1EV411x7P1"),
            ("扁形动物：躺不平 何以平天下", "BV1HT4y1r7KP"),
            ("异虫：我徘徊在地狱边缘，对死神说不", "BV1ti4y1A7q1"),
        ]
    },
    {
        "dir": "05_鱼类",
        "videos": [
            ("早期鱼类：亿年苦寒无人问，一朝出世四海平", "BV1Zt411n7qF"),
            ("软骨鱼：头铁真汉子 亿年五五开", "BV1SJ41137bu"),
            ("肉鳍鱼类：目标 陆地", "BV17t411g7Ni"),
            ("甲胄鱼：一鱼永生 万鱼陨落", "BV14xt2zFE3Z"),
            ("鲤形目：学好数理化，淡水称王霸", "BV1sx4y1A7ZD"),
            ("鲇形目：数值怪的养成之道", "BV1RN41177ex"),
        ]
    },
    {
        "dir": "06_两栖与海洋爬行动物",
        "videos": [
            ("离片椎类两栖动物：我有特殊的生存技巧", "BV1R4411r7AR"),
            ("鳍龙：迷惑演化造就世界最苟", "BV1YJ411h75d"),
            ("鱼龙：身世浮沉雨打萍", "BV1fJ411Q71L"),
            ("翼龙：大鹏一日同风起", "BV1qJ411x7oD"),
        ]
    },
    {
        "dir": "07_龙兽争霸",
        "videos": [
            ("龙兽争霸（其一）：开局一只兽 装备全靠莽", "BV1CE411y7G7"),
            ("龙兽争霸（其二）：时空狭缝中的异世界", "BV1BE411v7i1"),
            ("龙兽争霸（其三）：龙族巅峰", "BV1gJ411E7eA"),
            ("龙兽争霸（其四）：卧薪尝胆，兽虽三户可屠龙", "BV1dE411V7yB"),
            ("龙兽争霸（其五）：让恐龙再次伟大", "BV1nA411q7VG"),
            ("古颚类：最后的龙兽争霸", "BV1Qr4y1m7km"),
        ]
    },
    {
        "dir": "08_哺乳动物",
        "videos": [
            ("鲸：一曲鲸歌寄沧海", "BV1jv41167hr"),
            ("奇蹄目：看铁蹄铮铮，踏遍万里河山", "BV1rA411Y7fE"),
            ("偶蹄目：掌握核心黑科技", "BV1iK4y1a7k1"),
            ("长鼻目：大象无形", "BV1fu4y1o7UQ"),
            ("兔形目：喜马拉雅造就的不合理生物", "BV1XM411w7VM"),
            ("食肉目：猫与犬之歌，权力的游戏", "BV1nA411u7JL"),
            ("蝙蝠：我们仍未知道那天蝙蝠是怎么起飞的", "BV1X7411b7Yc"),
            ("有袋类：我拿到了主角剧本却没有主角光环", "BV1fX4y1T7EW"),
            ("灵长类（其一）：被错爱的也有恃无恐", "BV1T5411E7wn"),
            ("灵长类（其二）：人之初", "BV1UN411Q7k3"),
        ]
    },
    {
        "dir": "09_器官与系统演化",
        "videos": [
            ("神经演化（其一）：风起青萍之末", "BV14F411b7vm"),
            ("神经演化（其二）：混沌一念心智开", "BV1fY4y1s7dw"),
            ("神经演化（其三）：脑的夺权之路", "BV1ta41147nC"),
            ("神经演化（其四）：欲练此功 必先……", "BV13W4y1274W"),
            ("神经演化（其五）：脑智三分 所归于一", "BV13G411b7aH"),
            ("心脏与血液（其一）：天演之道 变化万千", "BV1HM4y1N7fq"),
            ("心脏与血液（其二）：天演之道 存乎一心", "BV1XA411c7nZ"),
            ("肺的演化（其一）：一息生两仪 两仪生万物", "BV1Pf421B77b"),
            ("肺的演化（其二）：福息？祸息？", "BV1kH4y1c7KR"),
            ("肺的演化（其三）：气吞万里如龙", "BV1waxYeHESd"),
            ("舌头演化史：从下岗边路到王牌辅助", "BV1WX4y1t7nv"),
            ("肌肉演化史：上古洪荒之力", "BV1U3411h7ZQ"),
        ]
    },
]


def safe_filename(title: str) -> str:
    """移除 Windows 文件名非法字符"""
    for ch in r'<>:"/\|?*':
        title = title.replace(ch, "_")
    return title


def create_structure():
    BASE.mkdir(parents=True, exist_ok=True)

    all_videos = []
    total = 0

    for cat in CATEGORIES:
        cat_dir = BASE / cat["dir"]
        cat_dir.mkdir(parents=True, exist_ok=True)
        print(f"[目录] {cat['dir']}")

        for i, (title, bv) in enumerate(cat["videos"], 1):
            total += 1
            safe = safe_filename(title)
            filepath = cat_dir / f"{safe}.md"
            url = f"https://www.bilibili.com/video/{bv}"
            cat_name = cat["dir"][3:]  # 去掉 "0X_" 前缀

            if not filepath.exists():
                content = f"""---
title: "{title}"
bv: "{bv}"
url: "{url}"
category: "{cat_name}"
series: "鬼谷说"
author: "芳斯塔芙 (鬼谷藏龙)"
status: pending
tags:
  - 鬼谷说
  - 生物演化
---

# {title}

> **BV号**: [{bv}]({url})
> **系列**: 鬼谷说
> **分类**: {cat_name}

---

## 转录文本

*待 FunASR 转写后填入*

---

## 笔记

-
"""
                filepath.write_text(content, encoding="utf-8")
                print(f"  [{i}] {safe}.md  [NEW]")
            else:
                print(f"  [{i}] {safe}.md  [SKIP] already exists")

            all_videos.append({
                "title": title,
                "bv": bv,
                "url": url,
                "category": cat_name,
                "dir": cat["dir"],
                "safe_filename": safe,
                "filepath": str(filepath),
            })

    # 导出视频列表 JSON
    json_path = BASE / "_video_list.json"
    json_path.write_text(
        json.dumps(all_videos, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"\n[EXPORT] _video_list.json ({total} entries)")

    # 创建总索引
    create_index(total)
    # 创建下载辅助 HTML
    create_download_html()

    print(f"\n=== DONE ===")
    print(f"Base: {BASE}")
    print(f"Categories: {len(CATEGORIES)} | Videos: {total}")
    print(f"\nStructure:")
    for cat in CATEGORIES:
        count = len(cat["videos"])
        print(f"  + {cat['dir']}/ ({count} videos)")
    print(f"  + _鬼谷说总索引.md")
    print(f"  + _video_list.json")
    print(f"  + _下载队列.html")


def create_index(total: int):
    lines = [
        "---",
        'title: "鬼谷说合集 — 总索引"',
        "tags: [索引, 鬼谷说, 生物演化]",
        "---",
        "",
        "# 鬼谷说合集 · 总索引",
        "",
        f"> 芳斯塔芙（鬼谷藏龙）B 站科普系列",
        f"> 共 **{total}** 期 · **{len(CATEGORIES)}** 个分类",
        "> 状态：⬜ pending = 待下载 | 🔄 active = 已转录 | ✅ complete = 完成",
        "",
        "---",
        "",
    ]

    for cat in CATEGORIES:
        cat_name = cat["dir"][3:]
        lines.append(f"## {cat['dir']}")
        lines.append("")
        lines.append("| # | 标题 | BV号 | 状态 |")
        lines.append("|---|------|------|------|")
        for i, (title, bv) in enumerate(cat["videos"], 1):
            safe = safe_filename(title)
            md_link = f"[{title}]({cat['dir']}/{safe}.md)"
            lines.append(f"| {i} | {md_link} | `{bv}` | ⬜ pending |")
        lines.append("")

    index_path = BASE / "_鬼谷说总索引.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[创建] _鬼谷说总索引.md")


def create_download_html():
    parts = [
        '<!DOCTYPE html>',
        '<html lang="zh-CN">',
        '<head>',
        '<meta charset="UTF-8">',
        '<title>鬼谷说 · 下载队列</title>',
        '<style>',
        '  body { font-family: "Microsoft YaHei", sans-serif; max-width: 960px; margin: 0 auto; padding: 20px; background: #1a1a2e; color: #e0e0e0; }',
        '  h1 { color: #e94560; border-bottom: 2px solid #e94560; padding-bottom: 10px; }',
        '  h2 { color: #e94560; background: #16213e; padding: 10px 15px; border-radius: 6px; margin: 25px 0 10px; }',
        '  .video-row { display: flex; align-items: center; padding: 6px 15px; border-bottom: 1px solid #2a2a4a; gap: 12px; }',
        '  .video-row:hover { background: #16213e; }',
        '  .num { width: 28px; color: #666; text-align: right; flex-shrink: 0; }',
        '  .title { flex: 1; }',
        '  .bv { font-family: Consolas, monospace; color: #e94560; font-size: 0.85em; flex-shrink: 0; }',
        '  .btn { color: #4ecca3; text-decoration: none; padding: 3px 12px; border: 1px solid #4ecca3; border-radius: 3px; font-size: 0.82em; flex-shrink: 0; }',
        '  .btn:hover { background: #4ecca3; color: #1a1a2e; }',
        '  .summary { background: #16213e; padding: 15px 20px; border-radius: 6px; margin-bottom: 20px; line-height: 1.8; }',
        '  .summary code { background: #0f3460; padding: 2px 6px; border-radius: 3px; }',
        '  .counter { float: right; color: #888; font-size: 0.9em; }',
        '</style>',
        '</head>',
        '<body>',
        '<h1>🦕 鬼谷说合集 · 下载队列</h1>',
        '<div class="summary">',
        f'  <strong>总计 {sum(len(c["videos"]) for c in CATEGORIES)} 期</strong> · {len(CATEGORIES)} 分类<br>',
        '  操作：点击「打开」→ 复制浏览器地址栏 URL → 粘贴到 <strong>jiidown</strong> → 下载为 mp3（最低音质）<br>',
        '  下载后文件位于：<code>D:\\jijidown(Bilibili video download tool)\\Download</code>',
        '</div>',
    ]

    for cat in CATEGORIES:
        count = len(cat["videos"])
        parts.append(f'<h2>{cat["dir"]} <span class="counter">{count} 期</span></h2>')
        for i, (title, bv) in enumerate(cat["videos"], 1):
            url = f"https://www.bilibili.com/video/{bv}"
            parts.append(
                f'<div class="video-row">'
                f'<span class="num">{i}</span>'
                f'<span class="title">{title}</span>'
                f'<span class="bv">{bv}</span>'
                f'<a class="btn" href="{url}" target="_blank">打开</a>'
                f'</div>'
            )

    parts.append('</body></html>')

    html_path = BASE / "_下载队列.html"
    html_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"[创建] _下载队列.html")


if __name__ == "__main__":
    create_structure()
