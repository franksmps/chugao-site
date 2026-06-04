@echo off
chcp 65001 >nul
echo ==========================================
echo   推送 CHUGAO 网站到 GitHub
echo ==========================================
echo.
echo GitHub 账号: franksmps
echo 仓库地址:   github.com/franksmps/chugao-site
echo.
echo 提示：本次推送会覆盖仓库中的旧版本网站文件。
echo.
echo 如果你还没有 GitHub Token:
echo 1. 打开 https://github.com/settings/tokens
echo 2. 点击 "Generate new token (classic)"
echo 3. 勾选 "repo" 权限（完整仓库读写）
echo 4. 生成后复制 Token（以 ghp_ 开头）
echo.
set /p TOKEN=请粘贴你的 GitHub Token: 
echo.
if "%TOKEN%"=="" (
    echo 错误: Token 不能为空。
    pause
    exit /b 1
)

echo 正在推送，请稍候...
git remote remove origin 2>nul
git remote add origin https://%TOKEN%@github.com/franksmps/chugao-site.git
git push -uf origin main

if %ERRORLEVEL% == 0 (
    echo.
    echo ==========================================
    echo   推送成功！
    echo   仓库地址: https://github.com/franksmps/chugao-site
    echo ==========================================
) else (
    echo.
    echo 推送失败，请检查 Token 是否正确，或网络是否通畅。
)

git remote remove origin 2>nul
git remote add origin https://github.com/franksmps/chugao-site.git

pause
