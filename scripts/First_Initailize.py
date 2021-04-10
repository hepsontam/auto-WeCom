from os import system
from os import getcwd

path = getcwd()
adb = path + '/platform-tools/adb.exe'

print('请首先确保电脑已经有线连接好测试设备\n')

deviceName = input('请输入测试设备的局域网IP地址： \n')
system(adb + ' tcpip 5555')
system(adb + ' connect ' + deviceName)
system(adb + ' devices')

input('\n请按回车键退出...')
quit()