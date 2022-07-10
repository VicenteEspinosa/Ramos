from backend_app.db_models.crmzone import CrmZone
from rest_framework import serializers


class CrmZoneSerializer(serializers.ModelSerializer):
    """CrmZone Serializer"""

    class Meta:
        model = CrmZone
        fields = (
            "id",
            "name",
        )
