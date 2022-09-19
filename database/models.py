from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=120)
    disc=models.TextField()
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
        