from django.db import models

# Create your models here.
class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    chapter_id = models.IntegerField()
    color = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    range1 = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    cfi = models.CharField(max_length=255)

