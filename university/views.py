from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializer
from library.crud_operations import CRUDOperations
from library.savefile import saveFile

# Create your views here.

class UniversityViews(APIView):
    def get(self,request,id=None):
        if id is None:
            response = CRUDOperations.getAllData(model=models.UniversityModel, serializer=serializer.UniversitySerializer)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversityModel, serializer=serializer.UniversitySerializer, university_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def post(self,request):
        university_details={
            **request.POST.dict(),
            'university_image' : 'image'
        }
        check_serializer=serializer.UniversitySerializer(data=university_details)
        if check_serializer.is_valid():
            university_details['university_image']=saveFile(path="university",file=request.FILES.get('university_image'))
            response = CRUDOperations.addNewData(serializer=serializer.UniversitySerializer, data=university_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'university_image' in request.POST:
            response = CRUDOperations.updateExistingDataUniv(model=models.UniversityModel, serializer=serializer.UniversitySerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            university_details={
            **request.POST.dict(),
            'university_image' : 'image'
            }
            check_serializer=serializer.UniversitySerializer(data=university_details,partial=True)
            if check_serializer.is_valid():
                university_details['university_image']=saveFile(path="university",file=request.FILES['university_image'])
                response=CRUDOperations.updateExistingDataUniv(model=models.UniversityModel, serializer=serializer.UniversitySerializer, id=id, data=university_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        response = CRUDOperations.deleteExistingDataUniv(model=models.UniversityModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class UniversityCourseView(APIView):
    def get(self,request,id=None):
        if id is None:
            u_id=request.headers['University-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversityCourseModel, serializer=serializer.UniversityCourseSerializer,university_id=u_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversityCourseModel, serializer=serializer.UniversityCourseSerializer, course_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.UniversityCourseSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataCou(model=models.UniversityCourseModel, serializer=serializer.UniversityCourseSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataCou(model=models.UniversityCourseModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class CourseDegreeView(APIView):
    def get(self,request,id=None):
        if id is None:
            c_id=request.headers['Course-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversityDegreeModel, serializer=serializer.UniversityDegreeSerializer,course_id=c_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversityDegreeModel, serializer=serializer.UniversityDegreeSerializer, degree_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.UniversityDegreeSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataDeg(model=models.UniversityDegreeModel, serializer=serializer.UniversityDegreeSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataDeg(model=models.UniversityDegreeModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DegreeYearView(APIView):
    def get(self,request,id=None):
        if id is None:
            d_id=request.headers['Degree-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversityYearModel, serializer=serializer.UniversityYearSerializer,degree_id=d_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversityYearModel, serializer=serializer.UniversityYearSerializer, year_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.UniversityYearSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataYrs(model=models.UniversityYearModel, serializer=serializer.UniversityYearSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataYrs(model=models.UniversityYearModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SemesterView(APIView):
    def get(self,request,id=None):
        if id is None:
            y_id=request.headers['Year-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversitySemesterModel, serializer=serializer.UniversitySemesterSerializer,year_id=y_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversitySemesterModel, serializer=serializer.UniversitySemesterSerializer, semester_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.UniversitySemesterSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataSem(model=models.UniversitySemesterModel, serializer=serializer.UniversitySemesterSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataSem(model=models.UniversitySemesterModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SemesterSubjectsView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Semester-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversitySubjectModel, serializer=serializer.UniversitySubjectSerializer,semester_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversitySubjectModel, serializer=serializer.UniversitySubjectSerializer, subject_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.UniversitySubjectSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataSub(model=models.UniversitySubjectModel, serializer=serializer.UniversitySubjectSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataSub(model=models.UniversitySubjectModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UniversityVideoView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversityVideoModel, serializer=serializer.UniversityVideoSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversityVideoModel, serializer=serializer.UniversityVideoSerializer, video_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        response = CRUDOperations.addNewData(serializer=serializer.UniversityVideoSerializer, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        response = CRUDOperations.updateExistingDataVid(model=models.UniversityVideoModel, serializer=serializer.UniversityVideoSerializer, id=id, data=request.data)
        if response['status']:
            return Response(data=response['data'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataVid(model=models.UniversityVideoModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UniversityFileView(APIView):
    def get(self,request,id=None):
        if id is None:
            s_id=request.headers['Subject-Id']
            response = CRUDOperations.getFilteredData(model=models.UniversityFileModel, serializer=serializer.UniversityFileSerializer,subject_id=s_id)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = CRUDOperations.getSpecificData(model=models.UniversityFileModel, serializer=serializer.UniversityFileSerializer, file_id=id)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        file_details={
            **request.POST.dict(),
            'file_url' : 'url'
        }
        check_serializer=serializer.UniversityFileSerializer(data=file_details)
        if check_serializer.is_valid():
            file_details['file_url']=saveFile(path="pdf_file",file=request.FILES.get('file_url'))
            response = CRUDOperations.addNewData(serializer=serializer.UniversityFileSerializer, data=file_details)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(check_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        if 'file_url' in request.POST:
            response = CRUDOperations.updateExistingDataFile(model=models.UniversityFileModel, serializer=serializer.UniversityFileSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            file_details={
            **request.POST.dict(),
            'file_url' : 'url'
            }
            check_serializer=serializer.UniversityFileSerializer(data=file_details,partial=True)
            if check_serializer.is_valid():
                file_details['file_url']=saveFile(path="pdf_file",file=request.FILES['file_url'])
                response=CRUDOperations.updateExistingDataFile(model=models.UniversityFileModel, serializer=serializer.UniversityFileSerializer, id=id, data=file_details)
                if response['status']:
                    return Response(data=response['data'],status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request, id):
        response = CRUDOperations.deleteExistingDataFile(model=models.UniversityFileModel, id=id)
        if response:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)