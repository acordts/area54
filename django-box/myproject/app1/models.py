from django.db import models

class Webcast(models.Model):
    title = models.CharField(max_length=256)


