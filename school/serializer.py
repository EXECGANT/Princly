from rest_framework.serializers import ModelSerializer
from . import models

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolModel
        fields = '__all__'
        
class SchoolClassSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolClassModel
        fields = '__all__'
        
class SchoolSubjectSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolSubjectModel
        fields = '__all__'
        
class SchoolvideoSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolVideoModel
        fields = '__all__'
        
class SchoolFileSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolFileModel
        fields = '__all__'