from djongo import models


class Datalist(models.Model):
    """Lists for metadata."""

    lists = models.JSONField() # {pickups: [str], work_types: [str], non_ok_options: [str]}
