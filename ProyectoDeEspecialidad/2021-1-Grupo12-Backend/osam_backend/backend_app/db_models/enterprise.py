from djongo import models


class Enterprise(models.Model):
    """Enterprise info for the technicians."""

    name = models.CharField(max_length=100)
