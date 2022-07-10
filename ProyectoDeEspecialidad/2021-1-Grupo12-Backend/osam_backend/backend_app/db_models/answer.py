from djongo import models


class Answers(models.Model):
    """Answer is the audit itself and its data."""

    auditor_id = models.IntegerField()
    commune_id = models.IntegerField()

    category_id = models.CharField(max_length=6)
    audit_type_id = models.CharField(max_length=6)
    service_type_id = models.CharField(max_length=6)
    exit_timestamp = models.DateTimeField(max_length=100)

    values = models.JSONField()
    metadata = models.JSONField()
    blocks = models.JSONField()
