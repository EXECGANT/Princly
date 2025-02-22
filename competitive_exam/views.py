from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializer
from library.crud_operations import CRUDOperations
from library.savefile import saveFile


# Create your views here.
class CompetitiveExamsView(APIView):
    def get(self,request,id=None):
        if id is None:
            response = CRUDOperations.getAllData(model=models.CompetitiveExamModel, serializer=serializer.CompettiiveExamSerializer)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.CompetitiveExamModel, serializer=serializer.CompettiiveExamSerializer, exam_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def post(self,request):
        exam_details={
            **request.POST.dict(),
            'exam_image' : 'image'
        }
        check_serializer=serializer.CompettiiveExamSerializer(data=exam_details)
        if check_serializer.is_valid():
            exam_details['exam_image']=saveFile(path="exam",file=request.FILES.get('exam_image'))
            print(exam_details)
            response = CRUDOperations.addNewData(serializer=serializer.CompettiiveExamSerializer, data=exam_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'exam_image' in request.POST:
            response = CRUDOperations.updateExistingDataExm(model=models.CompetitiveExamModel, serializer=serializer.CompettiiveExamSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            exam_details={
            **request.POST.dict(),
            'exam_image' : 'image'
            }
            check_serializer=serializer.CompettiiveExamSerializer(data=exam_details,partial=True)
            if check_serializer.is_valid():
                exam_details['exam_image']=saveFile(path="exam",file=request.FILES['exam_image'])
                response=CRUDOperations.updateExistingDataExm(model=models.CompetitiveExamModel, serializer=serializer.CompettiiveExamSerializer, id=id, data=exam_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        response = CRUDOperations.deleteExistingDataExm(model=models.CompetitiveExamModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ExamSubjectsView(APIView):
    def get(self,request,id=None):
        if id is None:
            e_id=request.headers['Exam-Id']
            response = CRUDOperations.getFilteredData(model=models.CompetitiveExamSubjectModel, serializer=serializer.CompetitiveExamSubjectSerializer,exam_id=e_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.CompetitiveExamSubjectModel, serializer=serializer.CompetitiveExamSubjectSerializer, subject_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.CompetitiveExamSubjectSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataSub(model=models.CompetitiveExamSubjectModel, serializer=serializer.CompetitiveExamSubjectSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataSub(model=models.CompetitiveExamSubjectModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ExamVideoView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.CompetitiveExamVideoModel, serializer=serializer.CompettiiveExamVideoSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.CompetitiveExamVideoModel, serializer=serializer.CompettiiveExamVideoSerializer, video_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.CompettiiveExamVideoSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataVid(model=models.CompetitiveExamVideoModel, serializer=serializer.CompettiiveExamVideoSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataVid(model=models.CompetitiveExamVideoModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ExamFileView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.CompetitiveExamFileModel, serializer=serializer.CompetitiveExamFileSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.CompetitiveExamFileModel, serializer=serializer.CompetitiveExamFileSerializer,file_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        file_details={
            **request.POST.dict(),
            'file_url' : 'url'
        }
        check_serializer=serializer.CompetitiveExamFileSerializer(data=file_details)
        if check_serializer.is_valid():
            file_details['file_url']=saveFile(path="pdf_file",file=request.FILES.get('file_url'))
            response = CRUDOperations.addNewData(serializer=serializer.CompetitiveExamFileSerializer, data=file_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'file_url' in request.POST:
            response = CRUDOperations.updateExistingDataFile(model=models.CompetitiveExamFileModel, serializer=serializer.CompetitiveExamFileSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            file_details={
            **request.POST.dict(),
            'file_url' : 'url'
            }
            check_serializer=serializer.CompetitiveExamFileSerializer(data=file_details,partial=True)
            if check_serializer.is_valid():
                file_details['file_url']=saveFile(path="pdf_file",file=request.FILES['file_url'])
                response=CRUDOperations.updateExistingDataFile(model=models.CompetitiveExamFileModel, serializer=serializer.CompetitiveExamFileSerializer, id=id, data=file_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataFile(model=models.CompetitiveExamFileModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)