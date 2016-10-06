from django.db import models

class Webcast(models.Model):
    guest_cnt = models.IntegerField(default=0)
