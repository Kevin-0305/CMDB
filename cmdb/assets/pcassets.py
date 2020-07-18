from rest_framework.views import APIView
from rest_framework.response import Response
from assets.models import pc_assets
from assets.serializers import PCAssetsSer
import json

class PCAssets(APIView):
    def get(self, request,*args,**kwargs):
        getData  = request.GET.dict()
        print(type(getData))
        print(getData)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': getData
        })


