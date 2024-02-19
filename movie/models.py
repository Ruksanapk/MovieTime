
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    plot = models.TextField()
    image = models.ImageField(upload_to="movies")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

