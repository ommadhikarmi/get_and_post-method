from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from models import *
from .serializer import *

# Create your views here.
class ResourceTypeView(ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    

class ResourcesView(GenericAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer

    def get(self,request):
        queryset =self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data  # the json data send in a request
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response('data is created')
        else:
            return Response(serializer.errors)
        
class DepartmentView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('department is created')
        else:
            return Response(serializer.errors)
        
class VendorView(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('vendor is created')
        else:
            return Response(serializer.errors)

class PurchaseView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(many=True)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('items has been purchase')
        else:
            return Response(serializer.errors)