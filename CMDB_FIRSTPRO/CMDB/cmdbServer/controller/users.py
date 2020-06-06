from rest_framework.views import APIView
from rest_framework.response import Response
# from django.forms.models import model_to_dict
from ..tools import modelToDict
from ..models import User as user
from ..connectDB import condb
from ..mapper.userMapper import UserMapper
import json



class Users(APIView):
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
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
        id = kwargs.get('id')
        retData= UserMapper().getUserById(id=id)
        return Response({
            'status': 200,
            'msg': 'ok',
            'results': retData
        })

    def post(self,request,*args,**kwargs):
        # data = json.loads(request.body)
        # print(request.POST.get('name'))
        if request.method == 'POST':
            data = request.data
            userObj = user()
            userDict = modelToDict(userObj,data=data)
            addID = UserMapper().insertUser(user=userDict)
            return Response({
                'status': 200,
                'msg': 'ok',
                'results': addID
            })

    def put(self,request,*args,**kwargs):
        # data = json.loads(request.body)
        # print(request.PUT.get('name'))
        data = request.data
        id = kwargs.get('id')
        data['id'] = id
        user = UserMapper().updateUser(user=data)
        return Response({
            'status': 200,
            'msg': 'ok',
            'results': user
        })

# def userSql(data):
#     sql = "inserter into cmdbServer_user set account={account},password={password}"
#     sql = sql.format_map(data)
#     print(sql)
     