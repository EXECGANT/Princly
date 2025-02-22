from rest_framework.serializers import ModelSerializer
from . import models

class ComputerCourseSerializer(ModelSerializer):
    class Meta:
        model = models.ComputerCourseModel
        fields = '__all__'
        
class ComputerCourseSubjectSerializer(ModelSerializer):
    class Meta:
        model = models.ComputerCourseSubjectModel
        fields = '__all__'
        
class ComputerCourseVideoSerializer(ModelSerializer):
    class Meta:
        model = models.ComputerCourseVideoModel
        fields = '__all__'
    
class ComputerFileSerializer(ModelSerializer):
    class Meta:
        model = models.ComputerFileModel
        fields = '__all__'