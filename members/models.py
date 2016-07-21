from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=64)
    short_bio = models.TextField(max_length=512) # Short Biography
    picture = models.ImageField(upload_to="members", default="members/py.png")

    def __str__(self):
        return self.name
