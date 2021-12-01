# serializers.py
from rest_framework import serializers

from .models import File, Provider

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id','first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id')

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('company', 'client_member_id', 'phone_number')

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = File
        fields = "__all__"