#!/usr/bin/python3
# -*- coding:utf-8 -*- 
import sqlite3

class Db(object):
    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.cursor = self.conn.cursor()

	def ddl(self, sql):
        self.cursor.execute(sql)
        self.close()
        return self.cursor.rowcount

    #SELECT、UPDATE、INSERT、DELETE
    def dml(self,sql):
        self.cursor.execute(sql)
        self.close()
        return self.cursor.fetchall()

    # 关闭
    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    Db()


# db = Db()
# db.ddl("insert into api (name, price,diff,tradeNum,tradePrice) values(1,1,1,1,1)")