from django.db import models
from djgeojson.fields import PointField


class Location(models.Model):
    wmoid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    geom = PointField()

    def __unicode__(self):
        return self.name