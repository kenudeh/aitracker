from rest_framework import serializers
from .models import *



class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')