from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    introduction = models.CharField(max_length=500)

    def to_dic(self):
        return {
            'id': self.id,
            'name': self.name,
            'introduction': self.introduction,
        }