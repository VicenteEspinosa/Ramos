from djongo import models


class AttZone(models.Model):
    """AttZone: location data"""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
