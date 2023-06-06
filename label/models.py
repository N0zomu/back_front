from django.db import models

# Create your models here.
class Label(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    book_id = models.CharField(max_length=20)
    chapter_id = models.CharField(max_length=20)
    cfi = models.CharField(max_length=20)
    percentage = models.IntegerField(default=0)
    time = models.DateTimeField(null=True)