from os import system
from os import getcwd

path = getcwd() 
filePath = path + '/python3.8.2/DeviceName.py'
ip = input('请输入新设备的局域网IP：\n')
cmd = 'echo ' + 'deviceName = "' + ip + ':5555" > ' + filePath
system(cmd)

print('\n设备IP修改完成\n')
print('设备名称(IP：端口号)：' + ip + ':5555')
print('保存文件路径： ' + filePath)

input('\n请按回车键退出...')
quit()