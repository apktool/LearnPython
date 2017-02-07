# 子进程|subprocess|Popen,communicate,returncode

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

'''
上述代码功能等价于下述指令集
nslookup
set q=mx
python.org
exit
'''
