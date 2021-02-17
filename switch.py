import os
import shutil

dir = "./BepInEx/plugins/"


def isDHHOpen():
    return os.path.exists("./BepInEx/plugins/DHH_AI4.dll")


def isDHHClose():
    return os.path.exists("./BepInEx/plugins/DHH_AI4.dll.disable")


def switchDHH(open):
    file = "./BepInEx/plugins/DHH_AI4.dll"
    file_disable = "./BepInEx/plugins/DHH_AI4.dll.disable"
    if(open):
        if(isDHHOpen()):
            print("DHH 插件已开启")
        elif(not isDHHClose()):
            print("DHH_AI4.dll.disable 不存在，请检查插件目录已存在，将覆盖")
        else:
            shutil.move(file_disable, file)
            print("DHH 插件已开启")
    else:
        if(not isDHHOpen()):
            print("DHH 插件已关闭")
        elif(isDHHClose()):
            print("DHH_AI4.dll.disable 已存在，将覆盖")
        else:
            shutil.move(file, file_disable)
            print("DHH 插件已关闭")

if __name__ == "__main__":
    if(not os.path.exists(dir)):
        print("没有检测到插件目录，请放置在HS2游戏根目录中!")
    else:
        a = input("请输入指令\n0    开启DHH\n1    关闭DHH\n")
        if(a == "0"):
            switchDHH(open=True)
        elif(a == "1"):
            switchDHH(open=False)
        else:
            print("输入格式错误")
    input("Press Any Key")
