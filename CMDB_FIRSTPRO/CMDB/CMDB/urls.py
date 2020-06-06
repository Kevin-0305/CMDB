"""CMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from cmdbServer.controller import users,server
from cmdbServer.controller.payment import ali_pay
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('docs/', include_docs_urls(title='站点页面标题')),
    path(r'docs/', get_swagger_view(title='API文档')),
    path('',TemplateView.as_view(template_name="index.html")),
    # path('pay',TemplateView.as_view(template_name="pay.html")),

    path('users/',users.Users.as_view()),
    path('user/',users.User.as_view()),
    path('user/<int:id>/',users.User.as_view()),

    path('servers/',server.Servers.as_view()),
    path('server/',server.Server.as_view()),
    path('server/<int:id>/',server.Server.as_view()),

    # path('pay',ali_pay.pay),
    # path('notify',ali_pay.updateOrder)
    path("pay",ali_pay.pay),
    # path("check_pay", ali_pay.check_pay)
]
