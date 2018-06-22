# -*- coding: UTF-8 -*-

import MySQLdb
import md_config
import md_logger
dbHost = md_config.getConfigDb('dbhost')
dbName = md_config.getConfigDb('dbname')
dbuser = md_config.getConfigDb('dbuser')
dbPasswd = md_config.getConfigDb('dbpasswd')
#这里要注意一下,port是int类型,否则会出错
dbPort = int(md_config.getConfigDb('dbport'))
dbCharset = md_config.getConfigDb('dbcharset')
mylog=md_logger.logger()
# noinspection PyGlobalUndefined
class MysqldbHelper:
    # 获取数据库连接
    @staticmethod
    def getCon():
        try:
            conn = MySQLdb.connect(host=dbHost,
                                   user=dbuser,
                                   passwd=dbPasswd,
                                   db=dbName,
                                   port=dbPort,
                                   charset=dbCharset,)
        except MySQLdb.Error as e:
            mylog.error("MysqldbError:%s" %e)
            print("MysqldbError:%s" % e)
            #conn=False
            # 查询方法，使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为字典
        return conn
    #执行sql，执行成功返回True,否则返回False
    def select(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor(MySQLdb.cursors.DictCursor)
            count=cur.execute(sql)
            if count>0:
                fc = cur.fetchall()
            else:
                fc=False
        except MySQLdb.Error as e:
            fc=False
            mylog.error("Mysqldb Error:%s" % e)
            print("Mysqldb Error:%s" % e)
            # 带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
        return fc

    def updateByParam(self, sql, params):
        count=0
        try:
            conn = self.getCon
            cursor = conn.cursor()
            count=cursor.execute(sql, params)
            conn.commit()
        except MySQLdb.Error as e:
            mylog.error("Mysqldb Error:%s" % e)
            print("Mysqldb Error:%s" % e)
        return count

    def update(self, sql):
        global connU
        try:
            connU = self.getCon()
            cursorU = connU.cursor()
            count = cursorU.execute(sql)
            connU.commit()
        except MySQLdb.Error as e:
            connU.rollback()
            mylog.error("Mysqldb Error:%s" % e)
            print("Mysqldb Error:%s" % e)
            count=0
        return count
    #下面是具体封装的sql语句方法
    #根据userId查询数据
    def queryId(self, userId):
        global queryId
        queryId = "select * from music_theme where id=%s" % userId
        fc = self.select(self,queryId)
        if  fc is False:
            print("您查询的数据不存在!")
        else:
            print("查询成功!")
            for row in fc:
                print(row)

    # 根据手机号查询数据
    def queryPhone(self, phone):
        queryPh = "select * from music_theme where order_num=%s" % phone
        fc = self.select(self, queryPh)
        if fc is False:
            print("您查询的数据不存在!")
        else:
            print("查询成功!")
            for row in fc:
                # print(row["id"])
                print(row)
    def ins(self):
        sql = "insert into pythontest values(5,'数据结构','this is a big book',now())"
        count = self.update(sql)
        print(count)

    def insparam(self):
        sql = "insert into pythontest values(%s,%s,%s,now())"
        params = (6, 'C#', 'good book')
        self.updateByParam(sql, params)

    def delop(self, userId):
        qyId = "select * from music_theme where id=%s" % userId
        fc = self.select(self, qyId)
        if fc is False:
            print("数据库中没有查询到该id数据!")
        else:
            sql = "delete from music_theme where id=%s" % userId
            count = self.update(self,sql)
            if count>0:
                print("数据删除成功!")
            else:print("数据删除失败!")


    def change(self, userId):
        queryId1 = "select order_num from music_theme where id=%s" % userId
        ft = self.select(self, queryId1)
        if ft is False:
            print("数据库中没有查询到该id数据!")
        else:
            for row in ft:
                num=row["order_num"]
            updateSql = "update sm_class set title=\'liang is not good boy\' where order_num=%s" % num
            count = self.update(self, updateSql)
            if count>0:
                print("数据更新成功!")
            else:print("数据没有更新!")
