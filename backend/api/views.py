from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import(
    ToolsSerializer
)
from .models import *



# Create your views here.
class ToolsView(generics.ListCreateAPIView):
    serializer_class = ToolsSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class SingleToolView(generics.RetrieveUpdateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    permission_classes = [IsAuthenticated]