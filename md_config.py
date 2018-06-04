import os
import configparser
#获取configdb配置文件
#其中os.path.split(os.path.realpath(__file__))是得到当前文件夹目录
def getConfig(section,key):
    config=configparser.ConfigParser()
    path=os.path.split(os.path.realpath(__file__))[0] + '/configdb.conf'
    config.read(path)
    return config.get(section,key)