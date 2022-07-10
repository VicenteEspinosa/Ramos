from djongo import models


class Question(models.Model):
    """The questions to make a form."""

    category = models.IntegerField(blank=True)
    options = models.JSONField() # {possible_values: []}
    value = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    category_id = models.IntegerField(blank=False)