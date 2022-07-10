from djongo import models


class Client(models.Model):
    """Client gets access to API reports."""

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    token = models.CharField(max_length=100)
