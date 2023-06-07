from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=20)
    book_introduction = models.CharField(max_length=100)
    book_main_type = models.CharField(max_length=50)
    book_secondary_type = models.CharField(max_length=50)
    book_author_name = models.CharField(max_length=20, default="")
    book_popularity = models.IntegerField()
    book_score = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    book_url = models.CharField(max_length=100)

    def to_dic(self):
        return {
            'book_id': self.book_id,
            'book_name': self.book_name,
            'book_introduction': self.book_introduction,
            'book_main_type': self.book_main_type,
            'book_secondary_type': self.book_secondary_type,
            'book_id': self.book_id,
            'book_name': self.book_name,
            'book_author_name': self.book_author_name,
            'book_popularity': self.book_popularity,
            'book_score': self.book_score,
            'book_url': self.book_url
        }