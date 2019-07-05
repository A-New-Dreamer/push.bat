import os
import sys
import time
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
    run('git init')
run('git add .')
print('请输入提交理由')
commit = input('提交理由: ')
if(commit == ''):
    run('git commit -m update')
else:
    run(('git commit -m',commit))
run('git push')