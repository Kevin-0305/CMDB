from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=200,verbose_name='账号',help_text='密码')
    password = models.CharField(max_length=200,verbose_name='密码',help_text='密码')
    name = models.CharField(max_length=200,verbose_name='用户名',help_text='用户名',blank=True,default='')

    class Mate:
        db_table = 'user'
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.name

class ServerData(models.Model):
    state_choices = (('0','关机'),('1','开启'))
    name = models.CharField(max_length=200,verbose_name='名字',help_text='名字')
    ip_address = models.CharField(max_length=200,verbose_name='ip地址',help_text='IP地址')
    ssh_port = models.IntegerField(verbose_name='ssh端口',help_text='ssh密码')
    account = models.CharField(max_length=200,verbose_name='登录账号',help_text='登录账号')
    password = models.CharField(max_length=200,verbose_name='登录密码',help_text='登录密码')
    state = models.IntegerField(choices=state_choices,default=0,verbose_name='当前状态',help_text='当前状态')
    description = models.CharField(max_length=200,verbose_name='描述',help_text='描述',blank=True)

    class Mate:
        db_table = 'server_data'
        verbose_name = "服务器信息表"
        verbose_name_plural = verbose_name
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.ip_address

class Goods(models.Model):
    name = models.CharField(max_length=200,verbose_name='商品',help_text='商品')
    price = models.FloatField(verbose_name='价格',help_text='价格')

    class Mate:
        db_table = 'goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.name

class Order(models.Model):
    order_id = models.BigIntegerField(verbose_name='订单id',help_text='订单id')
    goods_name = models.CharField(max_length=200, verbose_name='商品名',help_text='商品名')
    order_price = models.FloatField(verbose_name='订单价格',help_text='订单价格')
    goods_id = models.IntegerField(verbose_name='商品ID',help_text='商品ID ')
    is_pay = models.BooleanField(verbose_name='是否支付',help_text='是否支付')
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(verbose_name='支付时间',help_text='支付时间',blank=True,null=True)
    closed_time = models.DateTimeField(verbose_name = '交易关闭时间',help_text='交易关闭时间',blank=True,null=True)
    buyer_alipay_account = models.CharField(max_length=200,verbose_name='买家支付宝账号',help_text='买家支付宝账号',blank=True,null=True)

    class Mate:
        db_table = 'order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.order_id