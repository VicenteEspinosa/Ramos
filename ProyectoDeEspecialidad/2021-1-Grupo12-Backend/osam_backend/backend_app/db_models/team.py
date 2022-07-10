from djongo import models


class Team(models.Model):
    """The info about the technician groups."""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
