import time

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


#
#
# class User:
#     table_name = 'navigation_bar'
#
#     # 动态添加属性
#     def set_attr(self, **kwargs):
#         for k, v in kwargs.items():
#             self.__setattr__(k, v)
#
#     # 查询
#     def select(self):
#         sql = f"select * from {self.table_name}"
#         result = Mysql().query(sql)
#         return result
#
# # insert
# def insert(self, **kwargs):
#     keys = kwargs.keys()
#     values = kwargs.values()
#     keys = ",".join(keys)
#     values = "','".join(values)
#     sql = f"insert into {self.table_name}({keys}) values ('{values}')"
#     print(sql)
#     result = Mysql().execute(sql)
#     print(result)


# 封装一个模型类
# 增加一个field()方法来指定查询哪些列
class Model:

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k,v)

        self.table = self.__class__.__getattribute__(self, 'table_name')

    # 接收列名
    def field(self, columns):
        self.columns = columns
        return self

    # 带列名的查询操作
    def select(self, **kwargs):

        sql = f"select * from {self.table}"
        if hasattr(self, 'columns'):
            sql = f"select {self.columns} from {self.table}"
        if len(kwargs):
            sql += " where"
            for k, v in kwargs.items():
                sql += f" {k}='{v}' and"
            sql += " 1=1"
        print(sql)
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

    def delete(self):
        sql = f"delete from {self.table} where 1=1"
        print(sql)
        result = Mysql().execute(sql)
        print(result)


# 子类
class Users(Model):
    table_name = 'navigation_bar'
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)


if __name__ == '__main__':
    # user = User()
    # print(user.select())
    # user.insert(name='aboutus', url='tt')
    # user = Users(name='张三')
    # print(user.__getattribute__('name'))
    user = Users()
    # print(user.select(name='home'))
    # print(user.field('name,url').select(name='home'))
    # user.delete()
    # url_dict = {
    #     '首页': '/home',
    #     '关于我们': '/aboutus',
    #     '服务项': '/services',
    #     '图库': '/protfolio',
    #     '个人博客': '/blogsingle',
    #     '定价': '/pricing',
    #     '404': '/404',
    #     '所有博客': '/blog',
    #     '联系我们': '/contact',
    # }
    # for k, v in url_dict.items():
    #     user.insert(name=k, url=v)
    print(user.field("name,url").select())
