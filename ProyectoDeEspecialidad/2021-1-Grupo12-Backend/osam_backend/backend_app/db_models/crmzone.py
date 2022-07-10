from djongo import models


class CrmZone(models.Model):
    "CrmZone: location data"

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
