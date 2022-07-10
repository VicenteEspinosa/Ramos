from backend_app.db_models.block import Block
from rest_framework import serializers


class BlockSerializer(serializers.ModelSerializer):
    """Block serializer."""

    questions = serializers.JSONField(required=False)

    class Meta:
        """Meta."""

        model = Block
        fields = (
            "id",
            "name",
            "status",
            "questions",
            "category",
            "for_form"
        )

class BlockPutSerializer(serializers.ModelSerializer):
    """Block serializer without for_form and category."""

    questions = serializers.JSONField(required=False)

    class Meta:
        """Meta."""

        model = Block
        fields = (
            "id",
            "name",
            "status",
            "questions"
        )