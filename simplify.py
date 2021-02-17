import os
from collections import Counter
import functools
import hashlib
import shutil


def md5(file):
    m = hashlib.md5()  # 创建md5对象
    with open(file, 'rb') as fobj:
        while True:
            data = fobj.read(8192)
            if not data:
                break
            m.update(data)  # 更新md5对象

    return m.hexdigest()  # 返回md5对象


class Mod():

    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size
        self.md5_value = md5(path)

    def __str__(self):
        return "%s  %d" % (self.path, self.size)

    def __eq__(self, other):
        if self.name == other.name and self.size == other.size and self.md5_value == other.md5_value:
            return True
        return False

    def __hash__(self):
        return hash("%s  %d %s" % (self.name, self.size, self.md5_value))


def getMods(path):
    mods = []
    count = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            file = os.path.join(root, name)
            size = os.path.getsize(file)
            mods.append(Mod(name, file, size))
            count += 1
            print('\r读取Mod数量:{:d}'.format(count), end='')
    print("\n读取完成")
    return mods


if __name__ == "__main__":
    resDir = './mods/'
    try:
        if(os.path.exists(resDir)):
            print("检测到Mod目录:   %s" % (os.path.abspath(resDir)))
            mods = getMods(resDir)
            no_sim_mods = list(set(mods))
            mods_count = dict(Counter(mods))
            sim_mods_list = [key for key,
                             value in mods_count.items()if value > 1]
            print("原始数量:%d  去重后数量:%d   重复项:%d" %
                  (len(mods), len(no_sim_mods), len(sim_mods_list)))
            for mod in sim_mods_list:
                id = "%s   %d" % (mod.name, mod.size)
                print("\n"+id)
                sim_mods = [item for index, item in enumerate(
                    mods) if item == mod]
                sorted_sim_mods = sorted(
                    sim_mods, key=lambda item: -len(item.path))
                for sim_mod in sorted_sim_mods:
                    print(sim_mod)
                for delete_mod in sorted_sim_mods[1:]:
                    print("delete:  ", sim_mod)
                    os.remove(delete_mod.path)
        else:
            print("没有检测到Mod目录，请放到HS2游戏根目录下！")
    except:
        print("程序发生异常")
    finally:
        input("Press Any Key")
