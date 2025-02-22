from django.db import models

# Create your models here.
class CompetitiveExamModel(models.Model):
    exam_id=models.AutoField(primary_key=True)
    exam_name=models.TextField()
    exam_image=models.TextField()
    
class CompetitiveExamSubjectModel(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.TextField()
    exam_id=models.ForeignKey(CompetitiveExamModel, on_delete=models.CASCADE, null=False)
    
class CompetitiveExamVideoModel(models.Model):
    video_id=models.AutoField(primary_key=True)
    video_url=models.TextField()
    video_title=models.TextField(null=True)
    subject_id=models.ForeignKey(CompetitiveExamSubjectModel, on_delete=models.CASCADE, null=False)

class CompetitiveExamFileModel(models.Model):
    file_id=models.AutoField(primary_key=True)
    file_url=models.TextField()
    file_title=models.TextField(null=True)
    subject_id=models.ForeignKey(CompetitiveExamSubjectModel, on_delete=models.CASCADE, null=False)