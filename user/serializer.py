from rest_framework.serializers import ModelSerializer
from . import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ["id","user_name","user_email","password"]
    
class UserOTPSerializer(ModelSerializer):
    class Meta:
        model=models.UserModel
        fields=["otp"]
        
class UserDataSerializer(ModelSerializer):
    class Meta:
        model=models.UserModel
        fields='__all__'