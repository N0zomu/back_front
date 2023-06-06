from django.db import models

# Create your models here.

class User(models.Model):
<<<<<<< HEAD
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
=======
    user_id = models.AutoField(primary_key=True,default=1)
    user_name = models.CharField(max_length=20)
>>>>>>> 34b3b445979d35fdb4fde32e38116ad49e090aee
    password = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    ifManager = models.BooleanField()