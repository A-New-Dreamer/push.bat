import os
import sys
import time
try:
    if sys.argv[1] == 'build':
        if os.system('pyinstaller -v') == 0:
            os.system('pyinstaller -F push.py')
        else:
            os.system('pip install pyinstaller')
    elif sys.argv[1] == 'push':
        if sys.argv[2] == 'tags':
            os.system('git push --tags')
        elif sys.argv[2] == 'all':
            os.system('git add .')
            os.system('git commit -m "update"')
            os.system('git push')
            os.system('git push --tags')
        elif sys.argv[2] == 'commit':
            os.system('git add .')
            os.system('git commit -m "update"')
            os.system('git push')
except IndexError:
    def run(command):
        finish = os.system(command)
        if(finish == 0):
            pass
        else:
            print('系统错误')
            os.system('pause')
            os._exit(0)
    if(os.path.exists('./.git')):
        pass
    else:
        choose = input('未检测到.git文件夹，是否生成(yes or no) |yes|')
        if choose == 'y':
            run('git init')
        elif choose == 'yes':
            run('git init')
    run('git add .')
    print('请输入提交理由')
    commit = input('提交理由: ')
    if(commit == ''):
        run('git commit -m update')
    else:
        os.system(('git commit -m "'+commit+'"'))
    run('git push')