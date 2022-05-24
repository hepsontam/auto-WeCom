from os import system
from os import getcwd

path = getcwd() 
filePath = path + '\\DeviceName.txt'

# 添加IP地址
def appendName():
    deviceName = input('\n请输入新设备的局域网IP：\n')
    if deviceName!='' :                                   # 用户输入信息方有效
        with open(filePath, 'a') as f:                    # 打开/创建记录文本，此语法会自动关闭文件,‘a’为添加模式
            f.write('\n' + deviceName + ':5555')          # 添加用户输入的IP地址信息

        print('\n设备名称添加完成\n')
        print('设备名称(IP：端口号)：' + deviceName + ':5555')
        print('保存文件路径： ' + filePath)
        input('\n请按Enter返回...')
        system('cls')
    return 1

# 删除IP地址
def deleteName():
    indexDel = list(input('请输入欲删除的设备名称序号：').replace(' ', '')) # 可单次输入多个序号，并记作列表
    if indexDel!=[] :                                 # 用户输入信息方有效
        for n in range(len(indexDel)):                # 通过list批量删除元素
            del Text[int(indexDel[n])-n-1]            # 注意删除后索引号会相应变化
        with open(filePath, 'w') as f:                # ‘w’为写入模式
            f.truncate()                              # 清空文件原内容
        for n in range(len(Text)):                    # 将IP地址重新写入文件
            with open(filePath, 'a') as f:            # 创建记录文本，此语法会自动关闭文件,‘a’为添加模式              
                f.write(Text[n])                      # 添加用户输入的IP地址信息

        print('\n删除设备名称完成\n')
        print('保存文件路径： ' + filePath)
        input('\n请按Enter返回...')
        system('cls')
    return 1

while 1:
    print("\n\t\t设备记录表\n")
    print("\t序号 |" + "\t      设备名称")
    # 列举现有设备名称
    Text = open(filePath, mode='r').readlines()                        # 读取结果为list，如['......\n', '......']
    for n in range(len(Text)):                                         # 遍历设备
        deviceName = Text[n][Text[n].find("'")+1:Text[n].find(':')+5]  # 通过单引号和冒号截取设备名称
        print("\t " + str(n+1) + "     \t" + deviceName)


    print('\n可选择操作：1.添加设备名称  2.删除原有设备记录  3.退出')
    select = int(input('请输入操作序号：'))
 
    if select==1 :
        appendName()
    elif select==2 :
        deleteName()
    else:
        break
exit(0)



