git add .
set /p UserCommit="提交理由:"
if "%UserCommit%" == "" (
    git commit -m "update at %time%"
) else (
    git commit -m %UserCommit%
)
git push
pause