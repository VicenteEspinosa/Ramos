from djongo import models


class Commune(models.Model):
    """Commune: belongs to a Province"""

    name = models.CharField(max_length=100)
    province_id = models.IntegerField() 
    region_zona_att = models.IntegerField() 
    region_crm = models.IntegerField()
