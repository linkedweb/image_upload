from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.alt
