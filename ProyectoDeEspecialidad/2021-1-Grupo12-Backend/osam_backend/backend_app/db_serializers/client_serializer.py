from backend_app.db_models.client import Client
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    """Client serializer."""

    class Meta:
        """Meta."""

        model = Client
        fields = (
            "id",
            "name",
            "category",
            "token"
        )


class ClientPatchSerializer(serializers.ModelSerializer):
    """Client serializer without category."""

    class Meta:
        """Meta."""

        model = Client
        fields = (
            "id",
            "name",
            "token"
        )
