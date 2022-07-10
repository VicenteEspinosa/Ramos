from backend_app.db_models.report import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    """Report serializer."""

    blocks = serializers.JSONField(required=False)

    class Meta:
        """Meta."""

        model = Report
        fields = (
            "id",
            "name",
            "blocks",
            "question_based",
            "category",
            "for_api",
            "only_admin",
            "is_enumerated",
            "name_format",
        )
