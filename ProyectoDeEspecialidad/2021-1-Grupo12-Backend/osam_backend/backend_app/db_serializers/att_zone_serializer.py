from backend_app.db_models.att_zone import AttZone
from rest_framework import serializers


class AttZoneSerializer(serializers.ModelSerializer):
    """AttZone Serializer"""

    class Meta:
        model = AttZone
        fields = (
            "id",
            "name",
        )
