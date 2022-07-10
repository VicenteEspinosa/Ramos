from backend_app.db_models.answer import Answers
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    """Answer serializer."""

    values = serializers.JSONField(required=False)
    metadata = serializers.JSONField(required=False)
    blocks = serializers.JSONField(required=False)

    class Meta:
        """Meta."""

        model = Answers
        fields = (
            "id",
            "auditor_id",
            "commune_id",
            "category_id",
            "audit_type_id",
            "service_type_id",
            "exit_timestamp",
            "values",
            "metadata",
            "blocks",
        )
