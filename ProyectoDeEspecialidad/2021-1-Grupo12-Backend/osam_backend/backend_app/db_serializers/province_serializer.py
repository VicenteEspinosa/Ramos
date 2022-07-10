from backend_app.db_models.province import Province
from rest_framework import serializers


class ProvinceSerializer(serializers.ModelSerializer):
    """Province Serializer"""

    class Meta:
        """Meta"""

        model = Province
        fields = (
            "id",
            "name",
            "region_id",
        )
