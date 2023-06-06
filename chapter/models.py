from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField(default=0)
    chapter_no = models.IntegerField(default=0)
    chapter_name = models.CharField(max_length=100)
    chapter_href = models.CharField(max_length=100)

