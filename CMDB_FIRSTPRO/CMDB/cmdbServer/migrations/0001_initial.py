# Generated by Django 2.2.7 on 2020-05-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='名字', max_length=200, verbose_name='名字')),
                ('ip_address', models.CharField(help_text='IP地址', max_length=200, verbose_name='ip地址')),
                ('ssh_port', models.IntegerField(help_text='ssh密码', verbose_name='ssh端口')),
                ('account', models.CharField(help_text='登录账号', max_length=200, verbose_name='登录账号')),
                ('password', models.CharField(help_text='登录密码', max_length=200, verbose_name='登录密码')),
                ('state', models.IntegerField(choices=[('0', '关机'), ('1', '开启')], default=0, help_text='当前状态', verbose_name='当前状态')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=200, verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(help_text='密码', max_length=200, verbose_name='账号')),
                ('password', models.CharField(help_text='密码', max_length=200, verbose_name='密码')),
                ('name', models.CharField(help_text='用户名', max_length=200, verbose_name='用户名')),
            ],
        ),
    ]
