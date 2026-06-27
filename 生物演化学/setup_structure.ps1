# 鬼谷说合集 — Obsidian 目录结构生成器
# 生成日期: 2025-06-20
# 在 D:\obsidian\vault\生物演化学 下创建分类文件夹及 60 期视频的 markdown 骨架

$BASE = "D:\obsidian\vault\生物演化学"

# ========== 视频数据库 ==========
# 格式: @{Dir="分类目录名"; Videos=@(@{Title="标题"; BV="BV号"}, ...)}
$CATEGORIES = @(
    @{
        Dir = "01_节肢动物"
        Videos = @(
            @{Title="奇虾：初代霸主的故事"; BV="BV1wb41127jT"},
            @{Title="三叶虫：一个平凡家族的不屈与彷徨"; BV="BV1jb411H7aa"},
            @{Title="螯肢动物：死生一念 世路茫然"; BV="BV1n441147Wq"},
            @{Title="蜘蛛：结网的三重境界"; BV="BV1Hx4y1n7ts"},
            @{Title="昆虫：被偏爱的都有恃无恐"; BV="BV1X4411P7ce"},
            @{Title="蜚蠊目：飒爽奔跑在演化的夹缝中"; BV="BV1Yg9aB5ELN"},
            @{Title="鳞翅目：等待亿年的邂逅"; BV="BV1614y1a7cs"},
            @{Title="藤壶：那诡寄多端的过往……"; BV="BV1AX4y1J7TU"}
        )
    },
    @{
        Dir = "02_软体动物"
        Videos = @(
            @{Title="软体动物（其一）：家里有矿可劲儿浪"; BV="BV1gb411t7DT"},
            @{Title="软体动物（其二）：一场跨越三亿年的秘密战争"; BV="BV1Xb411M7br"},
            @{Title="软体动物（其三）：远古王者的不屈征途"; BV="BV1Sb411G726"},
            @{Title="蛸类：宿命的轮回"; BV="BV1JBFSecE2c"},
            @{Title="菊石（其一）：旧神的涅槃"; BV="BV16B4y1X7ap"},
            @{Title="菊石（其二）：此花开尽更无花"; BV="BV1TY4y157Hi"}
        )
    },
    @{
        Dir = "03_棘皮与腔肠动物"
        Videos = @(
            @{Title="棘皮动物：六亲不认的演化步伐"; BV="BV1Nb411h7bc"},
            @{Title="海胆：吾之演化 浑身是胆！"; BV="BV1voZ7BnEF1"},
            @{Title="水母：原初与彼方的超然魅影"; BV="BV1v4411L7Ee"}
        )
    },
    @{
        Dir = "04_海绵与蠕虫"
        Videos = @(
            @{Title="海绵：轮回引渡人"; BV="BV1Qh411E7LL"},
            @{Title="古蠕虫：历史的车辙"; BV="BV1EV411x7P1"},
            @{Title="扁形动物：躺不平 何以平天下"; BV="BV1HT4y1r7KP"},
            @{Title="异虫：我徘徊在地狱边缘，对死神说不"; BV="BV1ti4y1A7q1"}
        )
    },
    @{
        Dir = "05_鱼类"
        Videos = @(
            @{Title="早期鱼类：亿年苦寒无人问，一朝出世四海平"; BV="BV1Zt411n7qF"},
            @{Title="软骨鱼：头铁真汉子 亿年五五开"; BV="BV1SJ41137bu"},
            @{Title="肉鳍鱼类：目标 陆地"; BV="BV17t411g7Ni"},
            @{Title="甲胄鱼：一鱼永生 万鱼陨落"; BV="BV14xt2zFE3Z"},
            @{Title="鲤形目：学好数理化，淡水称王霸"; BV="BV1sx4y1A7ZD"},
            @{Title="鲇形目：数值怪的养成之道"; BV="BV1RN41177ex"}
        )
    },
    @{
        Dir = "06_两栖与海洋爬行动物"
        Videos = @(
            @{Title="离片椎类两栖动物：我有特殊的生存技巧"; BV="BV1R4411r7AR"},
            @{Title="鳍龙：迷惑演化造就世界最苟"; BV="BV1YJ411h75d"},
            @{Title="鱼龙：身世浮沉雨打萍"; BV="BV1fJ411Q71L"},
            @{Title="翼龙：大鹏一日同风起"; BV="BV1qJ411x7oD"}
        )
    },
    @{
        Dir = "07_龙兽争霸"
        Videos = @(
            @{Title="龙兽争霸（其一）：开局一只兽 装备全靠莽"; BV="BV1CE411y7G7"},
            @{Title="龙兽争霸（其二）：时空狭缝中的异世界"; BV="BV1BE411v7i1"},
            @{Title="龙兽争霸（其三）：龙族巅峰"; BV="BV1gJ411E7eA"},
            @{Title="龙兽争霸（其四）：卧薪尝胆，兽虽三户可屠龙"; BV="BV1dE411V7yB"},
            @{Title="龙兽争霸（其五）：让恐龙再次伟大"; BV="BV1nA411q7VG"},
            @{Title="古颚类：最后的龙兽争霸"; BV="BV1Qr4y1m7km"}
        )
    },
    @{
        Dir = "08_哺乳动物"
        Videos = @(
            @{Title="鲸：一曲鲸歌寄沧海"; BV="BV1jv41167hr"},
            @{Title="奇蹄目：看铁蹄铮铮，踏遍万里河山"; BV="BV1rA411Y7fE"},
            @{Title="偶蹄目：掌握核心黑科技"; BV="BV1iK4y1a7k1"},
            @{Title="长鼻目：大象无形"; BV="BV1fu4y1o7UQ"},
            @{Title="兔形目：喜马拉雅造就的不合理生物"; BV="BV1XM411w7VM"},
            @{Title="食肉目：猫与犬之歌，权力的游戏"; BV="BV1nA411u7JL"},
            @{Title="蝙蝠：我们仍未知道那天蝙蝠是怎么起飞的"; BV="BV1X7411b7Yc"},
            @{Title="有袋类：我拿到了主角剧本却没有主角光环"; BV="BV1fX4y1T7EW"},
            @{Title="灵长类（其一）：被错爱的也有恃无恐"; BV="BV1T5411E7wn"},
            @{Title="灵长类（其二）：人之初"; BV="BV1UN411Q7k3"}
        )
    },
    @{
        Dir = "09_器官与系统演化"
        Videos = @(
            @{Title="神经演化（其一）：风起青萍之末"; BV="BV14F411b7vm"},
            @{Title="神经演化（其二）：混沌一念心智开"; BV="BV1fY4y1s7dw"},
            @{Title="神经演化（其三）：脑的夺权之路"; BV="BV1ta41147nC"},
            @{Title="神经演化（其四）：欲练此功 必先……"; BV="BV13W4y1274W"},
            @{Title="神经演化（其五）：脑智三分 所归于一"; BV="BV13G411b7aH"},
            @{Title="心脏与血液（其一）：天演之道 变化万千"; BV="BV1HM4y1N7fq"},
            @{Title="心脏与血液（其二）：天演之道 存乎一心"; BV="BV1XA411c7nZ"},
            @{Title="肺的演化（其一）：一息生两仪 两仪生万物"; BV="BV1Pf421B77b"},
            @{Title="肺的演化（其二）：福息？祸息？"; BV="BV1kH4y1c7KR"},
            @{Title="肺的演化（其三）：气吞万里如龙"; BV="BV1waxYeHESd"},
            @{Title="舌头演化史：从下岗边路到王牌辅助"; BV="BV1WX4y1t7nv"},
            @{Title="肌肉演化史：上古洪荒之力"; BV="BV1U3411h7ZQ"}
        )
    }
)

# ========== 创建目录 ==========
Write-Host "=== 创建 Obsidian 鬼谷说目录结构 ===" -Foreground Cyan
Write-Host "基础路径: $BASE`n"

if (-not (Test-Path $BASE)) {
    New-Item -ItemType Directory -Path $BASE -Force | Out-Null
    Write-Host "[创建] $BASE"
}

$totalCount = 0
foreach ($cat in $CATEGORIES) {
    $dirPath = Join-Path $BASE $cat.Dir
    if (-not (Test-Path $dirPath)) {
        New-Item -ItemType Directory -Path $dirPath -Force | Out-Null
        Write-Host "[创建] $($cat.Dir)"
    }
    $totalCount += $cat.Videos.Count
}

Write-Host "`n总计分类: $($CATEGORIES.Count) | 视频: $totalCount"

# ========== 工具函数 ==========
function Get-SafeFileName($title) {
    # 移除 Windows 文件名非法字符，但保留中文
    $safe = $title -replace '[<>:/\|?*]', '_' -replace '"', "''"
    return $safe
}

function Get-TitleSlug($title) {
    # 提取主标题（冒号前部分），用于文件名匹配
    $title -replace '（[^）]*）', '' -replace '：.*$', '' -replace '[:：].*$', ''
}

# ========== 生成每个视频的 Markdown ==========
Write-Host "`n=== 生成视频 Markdown 骨架 ===" -Foreground Cyan

$allVideos = @()

foreach ($cat in $CATEGORIES) {
    $dirPath = Join-Path $BASE $cat.Dir
    foreach ($v in $cat.Videos) {
        $safeTitle = Get-SafeFileName $v.Title
        $filePath = Join-Path $dirPath "$safeTitle.md"
        $url = "https://www.bilibili.com/video/$($v.BV)"
        $slug = Get-TitleSlug $v.Title

        # 只创建不存在的文件（保护已填写的转录内容）
        if (-not (Test-Path $filePath)) {
            $content = @"
---
title: "$($v.Title)"
bv: "$($v.BV)"
url: "$url"
category: "$($cat.Dir -replace '^\d+_', '')"
series: "鬼谷说"
author: "芳斯塔芙 (鬼谷藏龙)"
date:
status: pending
tags:
  - 鬼谷说
  - 生物演化
---

# $($v.Title)

> **BV号**: [$($v.BV)]($url)
> **系列**: 鬼谷说
> **分类**: $($cat.Dir -replace '^\d+_', '')

---

## 转录文本

*待 FunASR 转写后填入*

---

## 笔记

-
"@
            $content | Out-File -FilePath $filePath -Encoding utf8
            Write-Host "  [新建] $($cat.Dir)/$safeTitle.md"
        } else {
            Write-Host "  [已存在] $($cat.Dir)/$safeTitle.md"
        }

        $allVideos += [PSCustomObject]@{
            Title = $v.Title
            BV = $v.BV
            URL = $url
            Category = $cat.Dir -replace '^\d+_', ''
            Dir = $cat.Dir
            Slug = $slug
            SafeFileName = $safeTitle
            FilePath = $filePath
        }
    }
}

# ========== 导出视频列表 JSON（供后续脚本使用）==========
$jsonPath = Join-Path $BASE "_video_list.json"
$allVideos | ConvertTo-Json -Depth 3 | Out-File -FilePath $jsonPath -Encoding utf8
Write-Host "`n[导出] 视频列表 → _video_list.json"

# ========== 创建总索引 ==========
Write-Host "`n=== 创建总索引 ===" -Foreground Cyan

$indexPath = Join-Path $BASE "_鬼谷说总索引.md"
$indexDate = Get-Date -Format "yyyy-MM-dd HH:mm"

$indexBody = @"
---
title: "鬼谷说合集 — 总索引"
date: $indexDate
tags:
  - 索引
  - 鬼谷说
  - 生物演化
---

# 鬼谷说合集 · 总索引

> 芳斯塔芙（鬼谷藏龙）B 站科普系列
> 共 $totalCount 期 · $($CATEGORIES.Count) 个分类
> 状态说明：pending = 待下载转写 | active = 已转录 | complete = 笔记完成

---

"@

foreach ($cat in $CATEGORIES) {
    $catName = $cat.Dir -replace '^\d+_', ''
    $indexBody += "`n## $($cat.Dir)`n`n"
    $indexBody += "| # | 标题 | BV号 | 状态 |`n"
    $indexBody += "|---|------|------|------|`n"
    $i = 1
    foreach ($v in $cat.Videos) {
        $safeTitle = Get-SafeFileName $v.Title
        $mdLink = "[$($v.Title)]($($cat.Dir)/$($safeTitle -replace ' ', '%20').md)"
        $indexBody += "| $i | $mdLink | ``$($v.BV)`` | ⬜ pending |`n"
        $i++
    }
}

$indexBody | Out-File -FilePath $indexPath -Encoding utf8
Write-Host "[创建] _鬼谷说总索引.md"

# ========== 创建下载辅助 HTML ==========
Write-Host "`n=== 创建下载辅助页 ===" -Foreground Cyan

$htmlPath = Join-Path $BASE "_下载队列.html"
$htmlHead = @"
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>鬼谷说 · 下载队列</title>
<style>
  body { font-family: 'Microsoft YaHei', sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; background: #1a1a2e; color: #e0e0e0; }
  h1 { color: #e94560; border-bottom: 2px solid #e94560; padding-bottom: 10px; }
  h2 { color: #0f3460; background: #16213e; padding: 10px 15px; border-radius: 5px; margin-top: 30px; }
  .video-item { display: flex; align-items: center; padding: 8px 15px; border-bottom: 1px solid #333; }
  .video-item:hover { background: #16213e; }
  .video-num { width: 30px; color: #888; }
  .video-title { flex: 1; }
  .video-bv { font-family: monospace; color: #e94560; margin: 0 15px; font-size: 0.9em; }
  .video-link { color: #4ecca3; text-decoration: none; padding: 3px 10px; border: 1px solid #4ecca3; border-radius: 3px; font-size: 0.85em; }
  .video-link:hover { background: #4ecca3; color: #1a1a2e; }
  .progress { color: #f0a500; margin: 20px 0; font-size: 0.9em; }
  .summary { background: #16213e; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
</style>
</head>
<body>
<h1>🦕 鬼谷说合集 · 下载队列</h1>
<div class="summary">
  <strong>总计: $totalCount 期</strong> · $($CATEGORIES.Count) 分类<br>
  <span class="progress">使用方法：点击链接在浏览器中打开 → 复制 URL → 粘贴到 jiidown 下载为 mp3</span><br>
  <strong>下载后存放路径：</strong><code>D:\jijidown(Bilibili video download tool)\Download</code>
</div>
"@

$htmlBody = ""
foreach ($cat in $CATEGORIES) {
    $htmlBody += "<h2>$($cat.Dir)</h2>`n"
    $i = 1
    foreach ($v in $cat.Videos) {
        $url = "https://www.bilibili.com/video/$($v.BV)"
        $htmlBody += @"
<div class="video-item">
  <span class="video-num">$i</span>
  <span class="video-title">$($v.Title)</span>
  <span class="video-bv">$($v.BV)</span>
  <a class="video-link" href="$url" target="_blank">打开</a>
</div>
"@
        $i++
    }
}

$htmlFoot = @"
</body>
</html>
"@

$htmlHead + $htmlBody + $htmlFoot | Out-File -FilePath $htmlPath -Encoding utf8
Write-Host "[创建] _下载队列.html (在浏览器中打开即可逐一下载)"

# ========== 总结 ==========
Write-Host "`n=== 完成 ===" -Foreground Green
Write-Host "目录: $BASE"
Write-Host "├── _鬼谷说总索引.md      ← Obsidian 总入口"
Write-Host "├── _video_list.json        ← 机读视频列表"
Write-Host "├── _下载队列.html          ← 浏览器下载辅助"
Write-Host "├── 01_节肢动物/            ($(($CATEGORIES | Where Dir -eq '01_节肢动物').Videos.Count) 期)"
Write-Host "├── 02_软体动物/            ($(($CATEGORIES | Where Dir -eq '02_软体动物').Videos.Count) 期)"
Write-Host "├── 03_棘皮与腔肠动物/      ($(($CATEGORIES | Where Dir -eq '03_棘皮与腔肠动物').Videos.Count) 期)"
Write-Host "├── 04_海绵与蠕虫/          ($(($CATEGORIES | Where Dir -eq '04_海绵与蠕虫').Videos.Count) 期)"
Write-Host "├── 05_鱼类/                ($(($CATEGORIES | Where Dir -eq '05_鱼类').Videos.Count) 期)"
Write-Host "├── 06_两栖与海洋爬行动物/  ($(($CATEGORIES | Where Dir -eq '06_两栖与海洋爬行动物').Videos.Count) 期)"
Write-Host "├── 07_龙兽争霸/            ($(($CATEGORIES | Where Dir -eq '07_龙兽争霸').Videos.Count) 期)"
Write-Host "├── 08_哺乳动物/            ($(($CATEGORIES | Where Dir -eq '08_哺乳动物').Videos.Count) 期)"
Write-Host "└── 09_器官与系统演化/      ($(($CATEGORIES | Where Dir -eq '09_器官与系统演化').Videos.Count) 期)"
Write-Host "`n下一步: 打开 _下载队列.html → 逐期下载到 jiidown → 运行后处理脚本"
