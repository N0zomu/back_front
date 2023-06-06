from django.db import models

# Create your models here.
class Star(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    book_id = models.CharField(max_length=20)