from djongo import models


class Form(models.Model):
    """Form is a list of block ids."""

    name = models.CharField(max_length=100)
    blocks = models.JSONField() # {block_ids: []}
    for_mobile = models.BooleanField(default=True)
    category = models.CharField(max_length=100)
    audit_type = models.CharField(max_length=100) 
    service_type = models.CharField(max_length=100)
