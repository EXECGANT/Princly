from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    # category_id=models.AutoField()
    category_name=models.TextField()
    category_image=models.TextField(null=True)
    