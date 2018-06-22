import logging.config
import md_config
import os
import time
from logging.handlers import RotatingFileHandler
format1 = md_config.getConfigLog("format").replace('@', '%')
backupcount = int(md_config.getConfigLog("backupcount"))
maxbytes=int(md_config.getConfigLog("maxbytes"))
level=int(md_config.getConfigLog("level"))
def logger():
    logger1 = logging.getLogger()
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    logpath=os.getcwd() + '/logs/' + rq + '.log'
    Rthandler = RotatingFileHandler(logpath, maxBytes=maxbytes, backupCount=backupcount, encoding='utf-8')
    # 这里来设置日志的级别
    # CRITICAl    50
    # ERROR    40
    # WARNING    30
    # INFO    20
    # DEBUG    10
    # NOSET    0
    logger1.setLevel(level)
    print("错误级别",level)
    formater = logging.Formatter(format1)
    Rthandler.setFormatter(formater)
    logger1.addHandler(Rthandler)
    return logger1