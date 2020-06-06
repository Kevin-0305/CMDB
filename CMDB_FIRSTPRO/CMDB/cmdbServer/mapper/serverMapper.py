from ..connectDB import condb

class ServerMapper():
    def getServers(self,**kwargs):
        sql = "select id,name,ip_address,ssh_port,account,password,state,description \
            from cmdbServer_serverdata"
        data = condb.getAll(sql)
        return data

    def getServerById(self,id,**kwargs):
        sql = "select id,name,ip_address,ssh_port,account,password,state,description \
            from cmdbServer_serverdata where id = {id}".format(id=id)
        data = condb.getOne(sql)
        return data

    def getServerByIP(self,ip,**kwargs):
        sql = "select id,name,ip_address,ssh_port,account,password,state,description \
            from cmdbServer_serverdata where ip_address = {ip}".format(ip=ip)
        data = condb.getAll(sql)
        return data
    
    def insertServer(self,server,**kwargs):
        sql = "insert into cmdbServer_serverdata (name,ip_address,ssh_port,account,password,state,description) \
            values ('{name}','{ip_address}',{ssh_port},'{account}','{password}',{state},'{description}')"
        sql = sql.format_map(server)
        print(sql)
        addID = condb.commitOne(sql)
        return addID

    def updateServer(self,server,**kwargs):
        sql = "update cmdbServer_serverdata set "
        if "name" in server.keys():
            sql = sql+" name={name},"
        if "ip_address" in server.keys():
            sql = sql + " ip_address ={ip_address},"
        if "ssh_port" in server.keys():
            sql = sql + " ssh_port ={ssh_port},"
        if "account" in server.keys():
            sql = sql + " account ={account},"
        if "password" in server.keys():
            sql = sql + " password ={password},"
        if "state" in server.keys():
            sql = sql + " state ={state},"
        if "description" in server.keys():
            sql = sql + " description ={description},"
        sql = sql[:-1]
        sql = sql + " where id = {id}" 
        sql = sql.format_map(server)
        condb.commitOne(sql)
        return server
    
    def deleteServer(self,id,**kwargs):
        sql = "delete from cmdbServer_serverdata where id = {id}".format(id=id)
        condb.commitOne(sql)
        


