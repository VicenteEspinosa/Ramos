from backend_app.db_models.info_panel import InfoPanel
from rest_framework import serializers


class InfoPanelSerializer(serializers.ModelSerializer):
    """InfoPanel serializer."""

    class Meta:
        """Meta."""

        model = InfoPanel
        fields = (
            "id",
            "timestamp",
            "auditor_id",
            "technician_id",
            "data_type",
            "auditor_name",
            "answer_id",
            "photos"
        )
