from rest_framework import serializers
from .models import *

class PCAssetsSer(serializers.ModelSerializer):
    class Meta:
        model  = pc_assets
        fields = "__all__"
