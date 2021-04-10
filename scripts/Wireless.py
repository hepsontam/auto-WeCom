# 本脚本使用无线连接，第一次运行请使用有线连接 >>> First_initialize.py

from os import system
from os import popen
from os import getcwd
from time import sleep
from DeviceName import deviceName

# 定位到项目中的adb.exe
path = getcwd()
adb = path + "/platform-tools/adb.exe"

# 连接设备
system(adb + " connect " + deviceName)

# 获取画面尺寸，进而定位
size = popen(str(adb + " -s " + deviceName + " shell wm size")).readline()

print(size)
row = int(size[-10:-6])
column = int(size[-5:])

location = {
    "workstation": (int(5*row/8), int(0.96*column)),
    "healthReport": (int((row+88)/6), int(0.42*column)),
    "write": (int(0.5*row), int(0.2*column)),
    "finish": (int(0.5*row), int(0.9*column))
}

# 通过包名启动 企业微信
system(adb+" -s " + deviceName + " shell am start com.tencent.wework/.launch.LaunchSplashEduActivity")
# zx
# system("adb shell am start -n com.tencent.wework/.permissionutil.PermissionActivity")
sleep(3)

# 通过坐标点击 工作台
system(adb + " -s " + deviceName + " shell input tap " + str(location["workstation"][0]) + " " + str(location["workstation"][1]))
sleep(1)

# 通过坐标点击 健康上报
system("adb -s " + deviceName + " shell input tap " + str(location["healthReport"][0]) + " " + str(location["healthReport"][1]))
sleep(3)

# 通过坐标点击 机电学院学生健康信息填报
system(adb + " -s " + deviceName + " shell input tap " + str(location["write"][0]) + " " + str(location["write"][1]))
# test使用
# system("adb shell input tap 525 700")
sleep(3)

# 滑动三次
system(adb + " -s " + deviceName + " shell input swipe 560 1500 560 600 200")
sleep(0.5)
system(adb + " -s " + deviceName + " shell input swipe 560 1500 560 600 200")
sleep(0.5)
system(adb + " -s " + deviceName + " shell input swipe 560 1500 560 600 200")
sleep(1)

# 通过坐标点击 确认提交
system(adb + " -s " + deviceName + " shell input tap " + str(location["finish"][0]) + " " + str(location["finish"][1]))
sleep(3)

# 通过虚拟返回键 返回
system(adb + " -s " + deviceName + " shell input keyevent 4")
sleep(1)
system(adb + " -s " + deviceName + " shell input keyevent 4")
sleep(1)

# 通过虚拟Home键 返回主界面
system(adb + " -s " + deviceName + " shell input keyevent 3")
# 退出 企业微信
system(adb + " -s " + deviceName + " shell am kill com.tencent.wework/.launch.LaunchSplashEduActivity")

# 关闭adb服务
system(adb + " kill-server")

quit()