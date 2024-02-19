from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from cloudinary.models import CloudinaryField
from rating.models import Rating


class Funfacts(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    ratings = GenericRelation(Rating)

    def __str__(self):
        return self.title
