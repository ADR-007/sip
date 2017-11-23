# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ["pk"]

    def __unicode__(self):
        return self.__str__()


### IMAGES ###
### IMAGES ###
### IMAGES ###
### IMAGES ###
### IMAGES ###


# from django.db import models
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill

# class Profile(models.Model):
#     avatar = models.ImageField(upload_to='avatars')
#     avatar_thumbnail = ImageSpecField(source='avatar',
#                                       processors=[ResizeToFill(100, 50)],
#                                       format='JPEG',
#                                       options={'quality': 60})

# profile = Profile.objects.all()[0]
# print profile.avatar_thumbnail.url    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
# print profile.avatar_thumbnail.width  # > 100





# size - max width and height, for example [640, 480]
# crop - resize and crop. ['top', 'left'] - top left corner, ['middle', 'center'] is center cropping, ['bottom', 'right'] - crop right bottom corner.
# quality - quality of resized image 1..100
# keep_meta - keep EXIF and other meta data, default True


# from django_resized import ResizedImageField

# class MyModel(models.Model):
#     ...
#     image1 = ResizedImageField(size=[500, 300], upload_to='whatever')
#     image2 = ResizedImageField(size=[100, 100], crop=['top', 'left'], upload_to='whatever')
#     image3 = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='whatever')
#     image4 = ResizedImageField(size=[500, 300], quality=75, upload_to='whatever')