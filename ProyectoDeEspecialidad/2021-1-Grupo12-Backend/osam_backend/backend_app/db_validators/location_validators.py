from backend_app.db_models.commune import Commune


def validate_commune(location_id):
    """location_id is the commune_id. Returns True if a commune with id == location_id exists"""

    commune = None
    try:
        commune = Commune.objects.get(id=location_id)
    except Commune.DoesNotExist:
        commune = None
    return commune is not None
