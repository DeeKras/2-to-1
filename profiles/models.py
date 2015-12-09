from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from utils  import GENDER_CHOICES


class Advocate(models.Model):
    username = models.OneToOneField(User)
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name_plural = 'advocates'

    def __unicode__(self):
        return u'{}: {}'.format(self.pk, self.email)

class Single_Profile(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              blank=False)
    age = models.IntegerField(blank=False)
    photo = models.ImageField(upload_to = 'photos/', default = 'photos/None/no-img.jpg')
    created_by = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    most_recent_change_id = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'singles'

    def __unicode__(self):
        return u'{}: {}, {}'.format(self.pk, self.lastname, self.firstname)


class Single_ChangeLog(models.Model):
    changed_by = models.ForeignKey(User)
    changed_date = models.DateTimeField(auto_now_add=True)

    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              blank=False)
    age = models.IntegerField(blank=False)
    photo = models.ImageField(upload_to = 'photos/', default = 'photos/None/no-img.jpg')

    class Meta:
        verbose_name_plural = 'single_changes'

    def __unicode__(self):
        return u'Changed {}: {}, {} on {}'.format(self.pk, self.lastname, self.firstname, self.changed_date)
