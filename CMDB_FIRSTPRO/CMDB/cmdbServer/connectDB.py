from django.db import connection

class condb(object):
    def getAll(sql,*args,**kwargs):
        cursor = connection.cursor()
        cursor.execute(sql,args)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return(data)

    def getOne(sql,*args,**kwargs):
        cursor = connection.cursor()
        cursor.execute(sql,args)
        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        data = dict(zip(columns, row))
        return(data)

    def commitOne(sql,*args,**kwargs):
        cursor = connection.cursor()
        cursor.execute(sql,args)    
        return({'id':cursor.lastrowid})

    def commitMany(sql,args):
        cursor = connection.cursor()
        cursor.executemany(sql,args)
        return({'id':cursor.lastrowid})
