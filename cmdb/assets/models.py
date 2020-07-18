from django.db import models

# Create your models here.

class pc_assets(models.Model):
    serial_num= models.CharField(max_length=20,verbose_name='资产编号',help_text='资产编号',blank=True,null=True)
    mac = models.CharField(max_length=20,verbose_name='mac地址',help_text='mac地址')
    ip_address=models.GenericIPAddressField(verbose_name='内网IP',help_text='内网IP')
    user = models.CharField(max_length=20,verbose_name='使用者',help_text='使用者')
    owner = models.CharField(max_length=20,verbose_name='拥有者',help_text='拥有者')
    configure = models.TextField(verbose_name="配置描述",help_text="配置描述")


    