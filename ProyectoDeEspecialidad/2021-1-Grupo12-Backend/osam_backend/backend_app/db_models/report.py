from djongo import models


class Report(models.Model):
    """Report is a structure of blocks ids."""

    name = models.CharField(max_length=100)
    blocks = models.JSONField()
    category = models.CharField(max_length=50)
    question_based = models.BooleanField(default=False)
    for_api = models.BooleanField(default=False)
    only_admin = models.BooleanField(default=False)
    is_enumerated = models.BooleanField(default=False)
    name_format = models.CharField(max_length=50)
