from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializer
from library.crud_operations import CRUDOperations
from library.savefile import saveFile


# Create your views here.
class ComputerCourseView(APIView):
    def get(self,request,id=None):
        if id is None:
            response = CRUDOperations.getAllData(model=models.ComputerCourseModel, serializer=serializer.ComputerCourseSerializer)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.ComputerCourseModel, serializer=serializer.ComputerCourseSerializer, course_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def post(self,request):
        course_details={
            **request.POST.dict(),
            'course_image' : 'image'
        }
        check_serializer=serializer.ComputerCourseSerializer(data=course_details)
        if check_serializer.is_valid():
            course_details['exam_image']=saveFile(path="computer_course",file=request.FILES.get('course_image'))
            response = CRUDOperations.addNewData(serializer=serializer.ComputerCourseSerializer, data=course_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'course_image' in request.POST:
            response = CRUDOperations.updateExistingDataCou(model=models.ComputerCourseModel, serializer=serializer.ComputerCourseSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            course_details={
            **request.POST.dict(),
            'course_image' : 'image'
            }
            check_serializer=serializer.ComputerCourseSerializer(data=course_details,partial=True)
            if check_serializer.is_valid():
                course_details['course_image']=saveFile(path="computer_course",file=request.FILES['course_image'])
                response=CRUDOperations.updateExistingDataCou(model=models.ComputerCourseModel, serializer=serializer.ComputerCourseSerializer, id=id, data=course_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        response = CRUDOperations.deleteExistingDataCou(model=models.ComputerCourseModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ComputerSubjectView(APIView):
    def get(self,request,id=None):
        if id is None:
            c_id=request.headers['Course-Id']
            response = CRUDOperations.getFilteredData(model=models.ComputerCourseSubjectModel, serializer=serializer.ComputerCourseSubjectSerializer,course_id=c_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.ComputerCourseSubjectModel, serializer=serializer.ComputerCourseSubjectSerializer, subject_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.ComputerCourseSubjectSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataSub(model=models.ComputerCourseSubjectModel, serializer=serializer.ComputerCourseSubjectSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataSub(model=models.ComputerCourseSubjectModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ComputerVideoView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.ComputerCourseVideoModel, serializer=serializer.ComputerCourseVideoSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.ComputerCourseVideoModel, serializer=serializer.ComputerCourseVideoSerializer, video_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.ComputerCourseVideoSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataVid(model=models.ComputerCourseVideoModel, serializer=serializer.ComputerCourseVideoSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataVid(model=models.ComputerCourseVideoModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ComputerFileView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.ComputerFileModel, serializer=serializer.ComputerFileSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.ComputerFileModel, serializer=serializer.ComputerFileSerializer,file_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        file_details={
            **request.POST.dict(),
            'file_url' : 'url'
        }
        check_serializer=serializer.ComputerFileSerializer(data=file_details)
        if check_serializer.is_valid():
            file_details['file_url']=saveFile(path="pdf_file",file=request.FILES.get('file_url'))
            response = CRUDOperations.addNewData(serializer=serializer.ComputerFileSerializer, data=file_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'file_url' in request.POST:
            response = CRUDOperations.updateExistingDataFile(model=models.ComputerFileModel, serializer=serializer.ComputerFileSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            file_details={
            **request.POST.dict(),
            'file_url' : 'url'
            }
            check_serializer=serializer.ComputerFileSerializer(data=file_details,partial=True)
            if check_serializer.is_valid():
                file_details['file_url']=saveFile(path="pdf_file",file=request.FILES['file_url'])
                response=CRUDOperations.updateExistingDataFile(model=models.ComputerFileModel, serializer=serializer.ComputerFileSerializer, id=id, data=file_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataFile(model=models.ComputerFileModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)