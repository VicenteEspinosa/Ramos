from backend_app.db_models.commune import Commune
from rest_framework import serializers


class CommuneSerializer(serializers.ModelSerializer):
    """Commune Serializer"""

    class Meta:
        """Meta"""

        model = Commune
        fields = (
            "id",
            "name",
            "province_id",
            "region_zona_att",
            "region_crm",
        )
