from django.db import models

# Create your models here.
class SchoolModel(models.Model):
    school_id=models.AutoField(primary_key=True)
    school_name=models.TextField()
    school_image=models.TextField()
    
class SchoolClassModel(models.Model):
    class_id=models.AutoField(primary_key=True)
    class_name=models.TextField()
    school_id=models.ForeignKey(SchoolModel, on_delete=models.CASCADE, null=False)
   
class SchoolSubjectModel(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.TextField()
    class_id=models.ForeignKey(SchoolClassModel, on_delete=models.CASCADE, null=False) 
    
class SchoolVideoModel(models.Model):
    video_id=models.AutoField(primary_key=True)
    video_url=models.TextField()
    video_title=models.TextField(null=True)
    subject_id=models.ForeignKey(SchoolSubjectModel, on_delete=models.CASCADE, null=False)

class SchoolFileModel(models.Model):
    file_id=models.AutoField(primary_key=True)
    file_url=models.TextField()
    file_title=models.TextField(null=True)
    subject_id=models.ForeignKey(SchoolSubjectModel, on_delete=models.CASCADE, null=False)