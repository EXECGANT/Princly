from django.db import models

# Create your models here.
class UserModel(models.Model):
    # user_id=models.AutoField(null=True)
    user_name=models.TextField()
    user_email=models.EmailField(unique=True)
    password=models.TextField()
    otp= models.CharField(max_length=6, unique=True)
    
    def __str__(self):
        return self.user_email
    
    
