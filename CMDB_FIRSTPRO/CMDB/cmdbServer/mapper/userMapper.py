from ..models import User as user
from ..connectDB import condb

class UserMapper():
    def insertUser(self,user,**kwargs):
        sql = "insert into cmdbServer_user (account,password,name) values ('{account}','{password}','{name}')"       
        sql = sql.format_map(user)
        addID =condb.commitOne(sql)
        return addID

    def getUsers(self,**kwargs):
        sql = "select id,account,name from cmdbServer_user where 1=1"
        data = condb.getAll(sql)
        return data

    def getUserById(self,id,**kwargs):
        sql = "select id,account,name from cmdbServer_user where 1=1  AND id = {id}".format(id=id)
        data = condb.getOne(sql)
        return data

    def getUserByAccount(self,account,**kwargs):
        sql = "select id,account,name from cmdbServer_user where 1=1  AND account = {account}".format(account=account)
        data = condb.getOne(sql)
        return data

    def updateUser(self,user,**kwargs):
        sql = "update cmdbServer_user set "
        if "account" in user.keys():
            sql = sql + " account = '{account}',"
        if "password" in user.keys():
            sql = sql + " password = '{password}',"
        if "name" in user.keys():
            sql = sql + " name = '{name}',"
        sql = sql[:-1]
        sql = sql + " where id = {id}" 
        sql = sql.format_map(user)
        print(sql)
        condb.commitOne(sql)
        return user
        

