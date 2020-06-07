from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect
import os
# from django.forms.models import model_to_dict
from ...tools import modelToDict
from ...models import Goods as goods
from ...models import Order as order
from ...models import ServerData as server
from ...connectDB import condb
from ...mapper.serverMapper import ServerMapper
import json

# from utils.Alipay import AliPay
from alipay import AliPay
import time
from datetime import datetime 


# def ali():
#     # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
#     app_id = "2016102200736333"
#     # POST请求，用于最后的检测(检测是否支付成功，生成订单)
#     notify_url = "http://vdotest.ha.cc:8080/notify"
#     # GET请求，用于页面的跳转展示（获取订单状态，显示给用户）
#     return_url = "http://vdotest.ha.cc:8080/pay"
#     # 用户的私钥
#     merchant_private_key_path = "keys/app_private_2048.txt"
#     # 支付宝的公钥
#     alipay_public_key_path = "keys/alipay_public_2048.txt"
#     sign_type="RSA2"
        
#     alipayClient = AliPay(
#         appid=app_id,
#         app_notify_url=notify_url,
#         # return_url=return_url,
#         app_private_key_path=merchant_private_key_path,
#         alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
#         debug=True,  # 默认False,
#     )
#     return alipayClient

# def buyGoods(request):
#     if request.method == 'GET':
#         alipay = ali()
#         uid = request.GET.get('uid')
#         goodsId = request.GET.get('goodsId')
#         goodsObject = goods.objects.get(id = goodsId)
#         goodsName = goodsObject.name
#         goodsPrice = goodsObject.price
#         orderObject = order()
#         orderObject.order_id = int(datetime.now().strftime('%Y''%m''%d''%H''%M''%S') + str(goodsId).rjust(2,'0'))
#         orderObject.name = goodsName
#         orderObject.order_price = goodsPrice
#         orderObject.goods_id = goodsId
#         orderObject.is_pay = False
#         orderObject.save()
#         query_params = alipay.direct_pay(
#             subject=goodsName,  # 商品简单描述
#             out_trade_no=str(orderObject.order_id),  # 商户订单号
#             total_amount=round(goodsPrice,2),  # 交易金额(单位: 元 保留俩位小数)
#         )
#         pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
#         print(pay_url)
        

#         return redirect(pay_url)

# def updateOrder(request):
#     alipay = ali()
#     if request.method == 'POST':
#         from urllib.parse import parse_qs
#         body_str = request.body.decode('utf-8')
#         post_data = parse_qs(body_str)
#         post_dict = {}
#         for k,v in post_data.items():
#             post_data[k] = v[0]
#         sign = post_dict.pop('sign',None)
#         status = alipay._verify(post_dict,sign)
#         print('------------------开始------------------')
#         print('POST验证', status)
#         print(post_dict)
#         out_trade_no = post_dict['out_trade_no']
#         # 修改订单状态
#         # models.Order.objects.filter(trade_no=out_trade_no).update(status=2)
#         print('------------------结束------------------')
#         # 修改订单状态：获取订单号
#         return Response({
#             'status': 0,
#             'msg': 'ok',
#             'results': "Post返回"
#         })
    

def pay(request):
    app_private_key_path = 'keys/app_private_2048.txt'
    alipay_public_key_path = "keys/alipay_public_2048.txt"
    alipay = AliPay(
    appid="2016102200736333",
    app_notify_url="http://127.0.0.1:8804/page2/",  # 默认回调url
    app_private_key_string=open(app_private_key_path).read(),
    alipay_public_key_string=open(alipay_public_key_path).read(),  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    sign_type="RSA2", # RSA 或者 RSA2
    debug=True,  # 默认False
    )
    order_string = alipay.api_alipay_trade_page_pay(
    # out_trade_no=datetime.now().strftime('%Y''%m''%d''%H''%M''%S'),
    out_trade_no="x2" + str(time.time()),
    total_amount=0.01,
    subject="充气式赵俊明",
    # notify_url="https://blog.csdn.net/" # 可选, 不填则使用默认notify url
    )
    pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    print(pay_url)
    return redirect(pay_url)



