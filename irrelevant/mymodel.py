import pymysql
from pymysql.cursors import DictCursor


class Mysql:

    def __init__(self):
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306, user='root',
                               passwd='123456',
                               charset='utf8',
                               database='lemonnt',
                               autocommit=True)
        self.cursor = conn.cursor(DictCursor)

    # 查询
    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    # 更新
    def execute(self, sql):
        try:
            self.cursor.execute(sql)
        except:
            return "fail"
        else:
            return "ok"


class User:
    table_name = 'navigation_bar'

    # 动态添加属性
    def set_attr(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    # 查询
    def select(self):
        sql = f"select * from {self.table_name}"
        result = Mysql().query(sql)
        return result

    # insert
    def insert(self, **kwargs):
        keys = kwargs.keys()
        values = kwargs.values()
        keys = ",".join(keys)
        values = "','".join(values)
        sql = f"insert into {self.table_name}({keys}) values ('{values}')"
        print(sql)
        result = Mysql().execute(sql)
        print(result)


if __name__ == '__main__':
    user = User()
    # print(user.select())
    user.insert(name='aboutus', url='tt')
