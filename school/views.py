from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializer
from library.crud_operations import CRUDOperations
from library.savefile import saveFile

# Create your views here.
class SchoolView(APIView):
    def get(self,request,id=None):
        if id is None:
            response = CRUDOperations.getAllData(model=models.SchoolModel, serializer=serializer.SchoolSerializer)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.SchoolModel, serializer=serializer.SchoolSerializer, school_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def post(self,request):
        school_details={
            **request.POST.dict(),
            'school_image' : 'image'
        }
        check_serializer=serializer.SchoolSerializer(data=school_details)
        if check_serializer.is_valid():
            school_details['school_image']=saveFile(path="school",file=request.FILES.get('school_image'))
            print(school_details)
            response = CRUDOperations.addNewData(serializer=serializer.SchoolSerializer, data=school_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'school_image' in request.POST:
            response = CRUDOperations.updateExistingDataSch(model=models.SchoolModel, serializer=serializer.SchoolSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            school_details={
            **request.POST.dict(),
            'school_image' : 'image'
            }
            check_serializer=serializer.SchoolSerializer(data=school_details,partial=True)
            if check_serializer.is_valid():
                school_details['school_image']=saveFile(path="school",file=request.FILES['school_image'])
                response=CRUDOperations.updateExistingDataSch(model=models.SchoolModel, serializer=serializer.SchoolSerializer, id=id, data=school_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        response = CRUDOperations.deleteExistingDataSch(model=models.SchoolModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SchoolClassView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['School-Id']
            response = CRUDOperations.getFilteredData(model=models.SchoolClassModel, serializer=serializer.SchoolClassSerializer,school_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.SchoolClassModel, serializer=serializer.SchoolClassSerializer, class_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.SchoolClassSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataCls(model=models.SchoolClassModel, serializer=serializer.SchoolClassSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataCls(model=models.SchoolClassModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SchoolSubjectsView(APIView):
    def get(self,request,id=None):
        if id is None:
            c_id=request.headers['class-Id']
            response = CRUDOperations.getFilteredData(model=models.SchoolSubjectModel, serializer=serializer.SchoolSubjectSerializer,class_id=c_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.SchoolSubjectModel, serializer=serializer.SchoolSubjectSerializer, subject_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.SchoolSubjectSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataSub(model=models.SchoolSubjectModel, serializer=serializer.SchoolSubjectSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataSub(model=models.SchoolSubjectModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SchoolVideoView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.SchoolVideoModel, serializer=serializer.SchoolvideoSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.SchoolVideoModel, serializer=serializer.SchoolvideoSerializer, video_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.SchoolvideoSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataVid(model=models.SchoolVideoModel, serializer=serializer.SchoolvideoSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataVid(model=models.SchoolVideoModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SchoolFileView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.SchoolFileModel, serializer=serializer.SchoolFileSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.SchoolFileModel, serializer=serializer.SchoolFileSerializer,file_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        file_details={
            **request.POST.dict(),
            'file_url' : 'url'
        }
        check_serializer=serializer.SchoolFileSerializer(data=file_details)
        if check_serializer.is_valid():
            file_details['file_url']=saveFile(path="pdf_file",file=request.FILES.get('file_url'))
            response = CRUDOperations.addNewData(serializer=serializer.SchoolFileSerializer, data=file_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'file_url' in request.POST:
            response = CRUDOperations.updateExistingDataFile(model=models.SchoolFileModel, serializer=serializer.SchoolFileSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            file_details={
            **request.POST.dict(),
            'file_url' : 'url'
            }
            check_serializer=serializer.SchoolFileSerializer(data=file_details,partial=True)
            if check_serializer.is_valid():
                file_details['file_url']=saveFile(path="pdf_file",file=request.FILES['file_url'])
                response=CRUDOperations.updateExistingDataFile(model=models.SchoolFileModel, serializer=serializer.SchoolFileSerializer, id=id, data=file_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataFile(model=models.SchoolFileModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)