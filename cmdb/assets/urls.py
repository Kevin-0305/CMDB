from django.contrib import admin
from django.urls import include, path
from assets.pcassets import PCAssets

urlpatterns = [
    path('pcAssets/',PCAssets.as_view()),
]