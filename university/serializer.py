from rest_framework.serializers import ModelSerializer
from . import models

class UniversitySerializer(ModelSerializer):
    class Meta:
        model = models.UniversityModel
        fields = '__all__'
        
class UniversityCourseSerializer(ModelSerializer):
    class Meta:
        model=models.UniversityCourseModel
        fields='__all__'

class UniversityDegreeSerializer(ModelSerializer):
    class Meta:
        model=models.UniversityDegreeModel
        fields='__all__'
        
class UniversityYearSerializer(ModelSerializer):
    class Meta:
        model=models.UniversityYearModel
        fields='__all__'

class UniversitySemesterSerializer(ModelSerializer):
    class Meta:
        model=models.UniversitySemesterModel
        fields='__all__'
        
class UniversitySubjectSerializer(ModelSerializer):
    class Meta:
        model=models.UniversitySubjectModel
        fields='__all__'
        
class UniversityVideoSerializer(ModelSerializer):
    class Meta:
        model=models.UniversityVideoModel
        fields='__all__'
    
class UniversityFileSerializer(ModelSerializer):
    class Meta:
        model=models.UniversityFileModel
        fields='__all__'