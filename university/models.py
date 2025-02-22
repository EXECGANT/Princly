from django.db import models

# Create your models here.
class UniversityModel(models.Model):
    university_id=models.AutoField(primary_key=True)
    university_name=models.TextField()
    university_image=models.TextField()
    
class UniversityCourseModel(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.TextField()
    university_id=models.ForeignKey(UniversityModel, on_delete=models.CASCADE, null=False)

class UniversityDegreeModel(models.Model):
    degree_id=models.AutoField(primary_key=True)
    degree_name=models.TextField()
    course_id=models.ForeignKey(UniversityCourseModel, on_delete=models.CASCADE, null=False)
    
class UniversityYearModel(models.Model):
    year_id=models.AutoField(primary_key=True)
    year_name=models.TextField()
    degree_id=models.ForeignKey(UniversityDegreeModel, on_delete=models.CASCADE, null=False)

class UniversitySemesterModel(models.Model):
    semester_id=models.AutoField(primary_key=True)
    semester_name=models.TextField()
    year_id=models.ForeignKey(UniversityYearModel, on_delete=models.CASCADE, null=False)
    
class UniversitySubjectModel(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.TextField()
    semester_id=models.ForeignKey(UniversitySemesterModel, on_delete=models.CASCADE, null=False)
    
class UniversityVideoModel(models.Model):
    video_id=models.AutoField(primary_key=True)
    video_url=models.TextField()
    video_title=models.TextField(null=True)
    subject_id=models.ForeignKey(UniversitySubjectModel, on_delete=models.CASCADE, null=False)

class UniversityFileModel(models.Model):
    file_id=models.AutoField(primary_key=True)
    file_url=models.TextField()
    file_title=models.TextField(null=True)
    subject_id=models.ForeignKey(UniversitySubjectModel, on_delete=models.CASCADE, null=False)