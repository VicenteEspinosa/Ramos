from backend_app.db_models.form_tree import FormTree
from rest_framework import serializers


class FormTreeSerializer(serializers.ModelSerializer):
    """Form tree serializer."""

    tree = serializers.JSONField(required=False)

    class Meta:
        """Meta."""

        model = FormTree
        fields = (
            "id",
            "tree",
        )
