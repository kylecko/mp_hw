from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics
from rest_framework.views import APIView
import io, csv, pandas as pd
from rest_framework.response import Response

from .serializers import FileSerializer, ProviderSerializer, FileUploadSerializer, SaveFileSerializer
from .models import File, Provider


class ClientViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class UploadFileViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File(
                        id = row['id'],
                        first_name= row["first_name"],
                        last_name= row['last_name'],
                        phone_number= row["phone_number"],
                        client_member_id= row["client_member_id"],
                        account_id= row["accound_id"]
                        )
            new_file.save()
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)


