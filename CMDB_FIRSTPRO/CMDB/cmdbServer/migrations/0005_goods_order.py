# Generated by Django 2.2.7 on 2020-06-05 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdbServer', '0004_auto_20200601_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='商品', max_length=200, verbose_name='商品')),
                ('price', models.FloatField(help_text='价格', verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(help_text='订单id', verbose_name='订单id')),
                ('goods_name', models.CharField(help_text='商品名', max_length=200, verbose_name='商品名')),
                ('order_price', models.FloatField(help_text='订单价格', verbose_name='订单价格')),
                ('goods_id', models.IntegerField(help_text='商品ID ', verbose_name='商品ID')),
                ('is_pay', models.BooleanField(help_text='是否支付', verbose_name='是否支付')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('pay_time', models.DateTimeField(blank=True, help_text='支付时间', null=True, verbose_name='支付时间')),
                ('closed_time', models.DateTimeField(help_text='交易关闭时间', verbose_name='交易关闭时间')),
                ('buyer_alipay_account', models.CharField(blank=True, help_text='买家支付宝账号', max_length=200, null=True, verbose_name='买家支付宝账号')),
            ],
        ),
    ]