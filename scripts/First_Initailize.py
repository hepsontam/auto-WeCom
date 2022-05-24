from os import system
from os import getcwd

print('请首先确保电脑已经有线连接好测试设备\n')

path = getcwd()
cmd = path + "\\platform-tools\\adb.exe"
print("adb路径：" + cmd + "\n")

filePath = path + '\\DeviceName.txt'

deviceName = input('\n请输入新设备的局域网IP地址：\n')
if deviceName!='' :
    with open(filePath, 'a') as f:                     # 创建记录文本，此方法会自动关闭文件,‘a’为添加模式
        f.write('\n' + deviceName + ':5555')           # 记录输入的设备名称

    print('\n设备名称添加完成\n')
    print('设备名称(IP：端口号)：' + deviceName + ':5555')
    print('保存文件路径： ' + filePath)


system(cmd + ' tcpip 5555')                       # 统一设定端口号为5555
system(cmd + ' connect ' + deviceName + ':5555')  # adb连接设备
system(cmd + ' devices')                          # 列举已连接设备

input('\n请按回车键退出...')
quit()