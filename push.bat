git add .
set /p UserCommit="�ύ����:"
if "%UserCommit%" == "" (
    git commit -m "update at %time%"
) else (
    git commit -m %UserCommit%
)
git push
pause