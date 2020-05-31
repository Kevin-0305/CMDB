from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User as user
from .connectDB import condb
import json



class Users(APIView):
    def get(self,request,*args,**kwargs):
        sql = "select id,account,name from cmdbServer_user where 1=1"
        retData = condb.getAll(sql)
        return Response({
            'status': 200,
            'msg': 'ok',
            'results': retData
        })

    def post(self,request,*args,**kwargs):
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': []
        })

class User(APIView):
    def get(self,request,*args,**kwargs):
        id = request.GET.get('id',None)
        sql = "select id,account,name from cmdbServer_user where 1=1 and id =%s"
        retData= condb.getOne(sql,id)
        return Response({
            'status': 200,
            'msg': 'ok',
            'results': retData
        })

    def post(self,request,*args,**kwargs):
        # data = json.loads(request.body)
        # print(request.POST.get('name'))
        data = request.data
        print(data)
        print(type(data))
        userSql(data)
        return Response({
            'status': 200,
            'msg': 'ok',
            'results': data
        })

    def put(self,request,*args,**kwargs):
        # data = json.loads(request.body)
        # print(request.PUT.get('name'))
        print(kwargs)
        data = request.data
        print(data)
        print(type(data))
        return Response({
            'status': 200,
            'msg': 'ok',
            'results': data
        })

def userSql(data):
    sql = "inserter into cmdbServer_user set account={account},password={password}"
    sql = sql.format_map(data)
    print(sql)
     