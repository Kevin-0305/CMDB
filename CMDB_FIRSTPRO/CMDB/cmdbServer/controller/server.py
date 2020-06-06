from rest_framework.views import APIView
from rest_framework.response import Response
# from django.forms.models import model_to_dict
from ..tools import modelToDict
from ..models import ServerData as server
from ..connectDB import condb
from ..mapper.serverMapper import ServerMapper
import json

class Servers(APIView):
    def get(self,request,*args,**kwargs):
        retData = ServerMapper().getServers()
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': retData
        })

class Server(APIView):
    def get(self,request,*args,**kwargs):
        id = request.GET.get(id)
        retData = ServerMapper().getServerById(id=id)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': retData
        })
    def post(self,request,*args,**kwargs):
        data = request.data
        serverObj = server()
        serverDict = modelToDict(serverObj,data=data)
        addID = ServerMapper().insertServer(server=serverDict)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': addID
        })
    def put(self,request,*args,**kwargs):
        id = kwargs.get('id')
        data = request.data
        data['id']= id
        server = ServerMapper().updateServer(server=data)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': server
        })
    def delete(self,request,*args,**kwargs):
        id = kwargs.get('id')
        server = ServerMapper().deleteServer(id=id)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': server
        })
