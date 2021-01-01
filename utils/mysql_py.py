import pymysql
from iatf.iatf.utils.read_config import ReadConfig
configs = ReadConfig()


class My_pymysql():
    def __init__(self):
        self.host = configs.config('database.hostname')
        self.user = configs.config('database.user')
        self.pwd = configs.config('database.pwd')
        self.db = configs.config('database.db')
        self.port = configs.config('database.port')
        self._connect()

    def _connect(self):
        try:
            self.conn = pymysql.connect(self.host,self.user,self.pwd,self.db,self.port)
            self.cur = self.conn.cursor()
        except pymysql.MySQLError as e:
            print(e)

    def table(self, table_name):
        '''
        :param table_name: 表名
        :return:
        '''
        self.table_name = table_name
        return self

    def field(self, field_name):
        '''
        :param field_name: 字段
        :return:
        '''
        self.field_name = field_name
        return self

    def where(self, field, option, param):
        '''
        :param where_name: 条件
        :return:
        '''
        sql = 'select {} from {} where {} {} %s'.format(self.field_name,self.table_name,field,option)
        self.cur.execute(sql, [param])
        res = self.cur.fetchone()
        print(sql)
        return res[0]

    def select_one(self,sql,params=None):
        try:
            self.cur.execute(sql,params)
            res = self.cur.fetchone()
            return res
        except pymysql.MySQLError as e:
            print(e)

    def select_all(self,sql):
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            return res
        except pymysql.MySQLError as e:
            print(e)

    def insert(self,sql):
        try:
            res = self.cur.execute(sql)
            self.conn.commit()
            # 返回插入的行数
            return res
        except pymysql.MySQLError as e:
            self.conn.rollback()
            print(e)

    def update(self,sql,params=None):
        try:
            res = self.cur.execute(sql,params)
            self.conn.commit()
            # 返回更新的行数
            return res
        except pymysql.MySQLError as e:
            self.conn.rollback()
            print(e)

    def delete(self,sql,params=None):
        try:
            res = self.cur.execute(sql,params)
            self.conn.commit()
            # 返回删除的行数
            return res
        except pymysql.MySQLError as e:
            self.conn.rollback()
            print(e)

    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    try:
        db = My_pymysql()
        # res = db.select_all('select * from statistics')
        # print(res)
        res = db.table('t_student_info').field('studentname').where('id','>','1001')
        print(res)
    except Exception as e:
        print(e)
#     try:
#         db = My_pymysql('192.168.31.194','root','root','test',3306)
#         res = db.connect()
#         # res = db.select_all('select * from test_1')
#         print(res)
#     except Exception as e:
#         print(e)

    # sql = "select * from test_1 where id = %s"%("'' or 1=1")
    # sql = "select * from test_1 where id = 5"
    # res = db.select_all(sql)
    # print(res)

    # sql_insert = "insert into test_1(case_name) values('测试1414')"
    # res = db.insert(sql_insert)
    # print(res)
    #
    # sql_select = "select * from test_1 order by id desc limit 0,1"
    # res = db.select_one(sql_select)
    # print(res)

    # sql_update = "update test_1 set case_name = '测试1442' where id=16"
    # res = db.update(sql_update)
    # print(res)

    # sql_delete = "delete from test_1 where id > 7"
    # res = db.delete(sql_delete)
    # print(res)

# list_1 = list('123543385')
# len1 = len(list_1)
# for i in range(len1-1):
#     for j in range(i,len1-1):
#         if list_1[j] > list_1[j+1]:
#             list_1[j],list_1[j+1] = list_1[j+1],list_1[j]
# print(list_1)

# class MyClass:
#     __secret_value = 1
#     _secret_value1 = 1
#
#     def __secter_method(self):
#         return '私有方法！'
# instance_of = MyClass()
# print(instance_of.__secret_value)
# print(instance_of._secret_value1)
# print(dir(MyClass))
# print(instance_of._MyClass__secter_method()) # 访问私有方法
# print(instance_of._MyClass__secret_value) # 访问私有属性


import pymysql,random,string

def randstr(len1,len2):
    str_1 = string.ascii_letters + string.digits
    str_2 = ''
    for i in range(random.randint(len1,len2)):
        str_2 += random.choice(str_1)
    return str_2

def randnum(len1,len2):
    str_1 = string.digits
    str_2 = ''
    for i in range(random.randint(len1,len2)):
        str_2 += random.choice(str_1)
    return str_2

def db_connect(host,user,pwd,db,port):
    try:
        conn = pymysql.connect(host,user,pwd,db,port)
        return conn
    except pymysql.MySQLError as e:
        print('数据库连接失败：%s'%e)

def insertmany(times):
    conn = db_connect('192.168.31.194','root','root','test',3306)
    try:
        cur = conn.cursor()
        for i in range(times):
            name_1 = randstr(6,8)
            age_1 = random.randint(18,60)
            sql_insert = "insert into test_1(`name`,`age`) values(%s,%s)"
            params = [name_1,age_1]
            cur.execute(sql_insert,params)
        conn.commit()
    except pymysql.MySQLError as e:
        conn.rollback()
        print(e)
    finally:
        cur.close()
        conn.close()

# insertmany(100)