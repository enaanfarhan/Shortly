from django.db import models
from .views import *
# Create your models here.


class shortlyURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    update = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        super(shortlyURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)