import logging.config
import md_config as myConfig
import os
import time
from logging.handlers import RotatingFileHandler
#日志内容的格式
class myLog:
    def __init__(self):
        global format1, maxBytes, backupCount, logLevel , logPath, rq
        format1 = myConfig.getConfigLog("format").replace('@', '%')
        #日志大小和数目
        backupCount = int(myConfig.getConfigLog("backupcount"))
        maxBytes=int(myConfig.getConfigLog("maxbytes"))
        #日志级别
        logLevel=int(myConfig.getConfigLog("level"))
        #日志格式
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #日志存放路径
        logPath = os.getcwd() + '/logs/' + rq + '.log'
    #保存日志到文件的函数
    @staticmethod
    def logger():
        #myLog()
        #创建一个logger,并设置级别
        logger1 = logging.getLogger()
        logger1.setLevel(logLevel)
        if not logger1.handlers:
            #创建一个handler,用于写入文件
            Rthandler = RotatingFileHandler(logPath, maxBytes=maxBytes, backupCount=backupCount, encoding='utf-8')
            # 这里来设置日志的级别
            # CRITICAl    50
            # ERROR    40
            # WARNING    30
            # INFO    20
            # DEBUG    10
            # NOSET    0
            #Rthandler.setLevel(level)
            #定义handler的输出格式
            formater = logging.Formatter(format1)
            #给handler添加formatter
            Rthandler.setFormatter(formater)
            #给logger添加handler
            logger1.addHandler(Rthandler)
        return logger1