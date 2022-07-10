from djongo import models


class Block(models.Model):
    """Block is a list of question ids."""

    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    questions = models.JSONField() # {question_ids: [int]}
    category = models.IntegerField(blank=False)
    for_form = models.BooleanField(default=True)
