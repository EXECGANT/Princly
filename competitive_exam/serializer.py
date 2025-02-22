from rest_framework.serializers import ModelSerializer
from . import models

class CompettiiveExamSerializer(ModelSerializer):
    class Meta:
        model = models.CompetitiveExamModel
        fields = '__all__'
        
class CompetitiveExamSubjectSerializer(ModelSerializer):
    class Meta:
        model = models.CompetitiveExamSubjectModel
        fields = '__all__'
        
class CompettiiveExamVideoSerializer(ModelSerializer):
    class Meta:
        model = models.CompetitiveExamVideoModel
        fields = '__all__'
        
class CompetitiveExamFileSerializer(ModelSerializer):
    class Meta:
        model = models.CompetitiveExamFileModel
        fields = '__all__'