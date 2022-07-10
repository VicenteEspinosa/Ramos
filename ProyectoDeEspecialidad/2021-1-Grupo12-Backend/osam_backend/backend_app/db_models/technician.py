from djongo import models
import datetime


class Technician(models.Model):
    """Technician info."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    enterprise_id = models.IntegerField(blank=False)
    category_id = models.IntegerField(blank=False)
    email = models.EmailField(blank=True)
    team_group_id = models.IntegerField(blank=False)
    last_audit_date = models.DateTimeField(default=datetime.date.today)
