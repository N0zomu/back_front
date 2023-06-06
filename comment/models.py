from django.db import models

# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    book_id = models.CharField(max_length=20)
    rate = models.IntegerField(default=0)
    content = models.CharField(max_length=2000)