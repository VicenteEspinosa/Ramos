from backend_app.db_models.team import Team
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    """Team Group technician serializer."""

    class Meta:
        """Meta."""

        model = Team
        fields = (
            "id",
            "name",
            "code"
        )