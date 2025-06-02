from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='place_images/')
    image2 = models.ImageField(upload_to='place_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='place_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='place_images/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
