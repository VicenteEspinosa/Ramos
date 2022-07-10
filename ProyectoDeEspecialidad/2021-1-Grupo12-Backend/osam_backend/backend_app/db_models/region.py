from djongo import models


class Region(models.Model):
    """Region that contains communes."""

    name = models.CharField(max_length=100) # Ex: Metropolitana de Santiago
    region_ordinal = models.CharField(max_length=100) # Ex: RM
