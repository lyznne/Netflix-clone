from django.db import models
from django.utils import timezone

CHARS_LENGTH: int = 150

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=CHARS_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 


class Tag(models.Model):
    name = models.CharField( max_length=CHARS_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 

class Movie(models.Model):
    name = models.CharField( max_length=CHARS_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')
    date_created = models.DateField( default=timezone.now)

    def __str__(self):
        return self.name 
