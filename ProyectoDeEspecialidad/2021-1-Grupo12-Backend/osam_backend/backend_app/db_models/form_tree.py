from djongo import models


class FormTree(models.Model):
    """Tree for form filter selection."""

    tree = models.JSONField() # {category_id: {audit_type_id: {service_type_id: str}}}
