from djongo import models


class Metadata(models.Model):
    """Metadata info."""

    name = models.CharField(max_length=100) # lo que se impime en el header
    route = models.JSONField() # tiene la ruta para encontrar la metadata en answer
    category = models.JSONField() # Lista con las categorias para la que se usa
