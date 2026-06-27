@echo off
chcp 65001 >nul
title 鬼谷说 — 转录后处理

echo.
echo ========================================
echo   鬼谷说合集 - 转录后处理管道
echo ========================================
echo.

set DOWNLOAD_DIR=D:\jijidown(Bilibili video download tool)\Download
set BASE=D:\obsidian\vault\生物演化学

:: ============================================
:: 第 0 步：下载完整性预检
:: ============================================
echo ========================================
echo   第 0 步：下载完整性检查
echo ========================================
echo.

python "%BASE%\check_completeness.py"

echo.
echo --------------------------------------------------
if %ERRORLEVEL% equ 0 (
    echo   全部 60 期已就绪！开始转录。
) else (
    echo   发现缺失，上面列出了具体差哪些。
    echo.
    set /p CHOICE="是否继续对已有文件进行转录？(y/n): "
    if /i not "%CHOICE%"=="y" (
        echo 已取消。请继续下载，完成后重新运行本脚本。
        pause
        exit /b 0
    )
    echo 好的，将对已下载的文件进行转录...
)

echo.
echo ========================================
echo   第 1 步：运行 FunASR 批量转写
echo ========================================
echo.

if not exist "%DOWNLOAD_DIR%" (
    echo [ERROR] Download 目录不存在: %DOWNLOAD_DIR%
    pause
    exit /b 1
)

:: 检查是否有音频文件
dir "%DOWNLOAD_DIR%\*.mp3" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    dir "%DOWNLOAD_DIR%\*.m4a" >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        dir "%DOWNLOAD_DIR%\*.wav" >nul 2>&1
        if %ERRORLEVEL% neq 0 (
            echo [ERROR] Download 目录中没有找到音频文件
            pause
            exit /b 1
        )
    )
)

echo 找到音频文件，开始 FunASR 转写...
echo.

call "D:\funasr_project\run.bat" "%DOWNLOAD_DIR%"

if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] FunASR 转写出错，请检查错误信息
    pause
    exit /b 1
)

echo.
echo ========================================
echo   第 2 步：匹配转录到 Obsidian markdown
echo ========================================
echo.

set OUTPUT_DIR=%DOWNLOAD_DIR%\output
if not exist "%OUTPUT_DIR%" (
    echo [ERROR] FunASR 输出目录不存在: %OUTPUT_DIR%
    echo 尝试查找其他 output 位置...
    dir /s /b "%DOWNLOAD_DIR%\*.txt" 2>nul
    pause
    exit /b 1
)

python "%BASE%\pipeline.py" --input "%OUTPUT_DIR%"

if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] 管道处理出错
    pause
    exit /b 1
)

echo.
echo ========================================
echo   完成！
echo ========================================
echo.
echo 转录文本已写入 Obsidian vault:
echo   D:\obsidian\vault\生物演化学\
echo.
echo 打开 Obsidian 即可查看所有笔记。
echo.
pause
