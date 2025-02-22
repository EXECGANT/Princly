from django.db import models

# Create your models here.
class ComputerCourseModel(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.TextField()
    course_image=models.TextField()
    
class ComputerCourseSubjectModel(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.TextField()
    course_id=models.ForeignKey(ComputerCourseModel, on_delete=models.CASCADE, null=False)
    
class ComputerCourseVideoModel(models.Model):
    video_id=models.AutoField(primary_key=True)
    video_url=models.TextField()
    video_title=models.TextField(null=True)
    subject_id=models.ForeignKey(ComputerCourseSubjectModel, on_delete=models.CASCADE, null=False)
    
class ComputerFileModel(models.Model):
    file_id=models.AutoField(primary_key=True)
    file_url=models.TextField()
    file_title=models.TextField(null=True)
    subject_id=models.ForeignKey(ComputerCourseSubjectModel, on_delete=models.CASCADE, null=False)