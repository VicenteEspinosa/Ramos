from backend_app.db_models.form import Form
from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    """Form serializer."""
    
    blocks = serializers.JSONField(required=False)

    class Meta:
        """Meta."""

        model = Form
        fields = (
            "id",
            "name",
            "blocks",
            "for_mobile",
            "category",
            "audit_type",
            "service_type"
        )
