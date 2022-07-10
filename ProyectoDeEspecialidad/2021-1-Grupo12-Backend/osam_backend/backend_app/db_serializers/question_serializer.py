from backend_app.db_models.question import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    """Question serializer."""

    options = serializers.JSONField(required=False)
    
    class Meta:
        """Meta."""

        model = Question
        fields = (
            "id",
            "category",
            "options",
            "value", 
            "status",
            "category_id"
        )

class QuestionPutSerializer(serializers.ModelSerializer):
    """Question serializer without category_id."""

    options = serializers.JSONField(required=False)
    
    class Meta:
        """Meta."""

        model = Question
        fields = (
            "id",
            "category",
            "options",
            "value", 
            "status"
        )
