from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=200,verbose_name='账号',help_text='密码')
    password = models.CharField(max_length=200,verbose_name='密码',help_text='密码')
    name = models.CharField(max_length=200,verbose_name='用户名',help_text='用户名')

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
