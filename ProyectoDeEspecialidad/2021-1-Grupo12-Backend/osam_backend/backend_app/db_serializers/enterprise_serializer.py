from backend_app.db_models.enterprise import Enterprise
from rest_framework import serializers


class EnterpriseSerializer(serializers.ModelSerializer):
    """Enterprise serializer."""

    class Meta:
        """Meta."""

        model = Enterprise
        fields = (
            "id",
            "name"
        )
