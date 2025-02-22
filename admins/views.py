from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializer
from library.crud_operations import CRUDOperations
from library.savefile import saveFile
# Create your views here.
class AdminsView(APIView):
    def get(self,request):
        pass
    def post(self,request):
        pass
    def patch(self,request,id):
        pass
    def delete(self,request,id):
        pass
    
    
class CategoryView(APIView):
    def get(self,request,id=None):
        if id is None:
            response = CRUDOperations.getAllData(model=models.CategoryModel, serializer=serializer.CategorySerializer)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.CategoryModel, serializer=serializer.CategorySerializer, id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        category_data={
            **request.POST.dict(),
            'category_image' : 'image'
        }
        check_serializer=serializer.CategorySerializer(data=category_data)
        if check_serializer:
            category_data['category_image']=saveFile(path="category",file=request.FILES.get('category_image'))
            response = CRUDOperations.addNewData(serializer=serializer.CategorySerializer, data=category_data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'category_image' in request.POST:
            print("image")
            response = CRUDOperations.updateExistingData(model=models.CategoryModel, serializer=serializer.CategorySerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            
            category_data={
            **request.POST.dict(),
            'category_image' : 'image'
            }
            print(category_data)
            check_serializer=serializer.CategorySerializer(data=category_data,partial=True)
            if check_serializer.is_valid():
                category_data['category_image']=saveFile(path="category",file=request.FILES['category_image'])
                response=CRUDOperations.updateExistingData(model=models.CategoryModel, serializer=serializer.CategorySerializer, id=id, data=category_data)
                if response['status']:
                    print("checked")
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        response = CRUDOperations.deleteExistingData(model=models.CategoryModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    