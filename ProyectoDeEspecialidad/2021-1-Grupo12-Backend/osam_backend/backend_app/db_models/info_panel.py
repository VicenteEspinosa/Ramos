from djongo import models


class InfoPanel(models.Model):
    """Information panel."""

    timestamp = models.DateTimeField(max_length=100)
    auditor_id = models.IntegerField()
    technician_id = models.IntegerField()
    answer_id = models.IntegerField()
    data_type = models.IntegerField()
    auditor_name = models.CharField(max_length=200)
    answer_id = models.IntegerField()
    photos = models.IntegerField()