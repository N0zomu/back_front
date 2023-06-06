from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=20)
    book_introduction = models.CharField(max_length=100)
    book_main_type = models.CharField(max_length=50)
    book_secondary_type = models.CharField(max_length=50)
    book_popularity = models.IntegerField()
    book_score = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
