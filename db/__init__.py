import pymysql

import settings


class DB():
    def __init__(self):
        self.db = pymysql.connect(**settings.DATABASE.get('default'))
        self.cursor = self.db.cursor()

    def save(self,item):
        if self.exist('user',item.id):
            return
        self.cursor.execute("insert into user(id,name,age,img,home) VALUES (%s,%s,%s,%s,%s)",
                            args=(item.id,item.name,item.age,item.img,item.home))
        if self.cursor.rowcount:
            print(item.name,'数据保存成功！')
            self.db.commit() # 提交事务

    def exist(self,tableName,id):
        self.cursor.execute("select in from {} WHERE id = %s".format(tableName),
                            args=(id))
        return self.cursor.rowcount >= 1

    def close(self):
        self.db.close() # 关闭数据库连接