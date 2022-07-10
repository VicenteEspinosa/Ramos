from djongo import models


class Province(models.Model):
    """Province: belongs to a Region"""

    name = models.CharField(max_length=100)
    region_id = models.IntegerField()
