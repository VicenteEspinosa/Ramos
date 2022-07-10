from backend_app.db_models.region import Region
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    """Region Serializer"""

    class Meta:
        """Meta"""

        model = Region
        fields = (
            "id",
            "name",
            "region_ordinal"
        )
