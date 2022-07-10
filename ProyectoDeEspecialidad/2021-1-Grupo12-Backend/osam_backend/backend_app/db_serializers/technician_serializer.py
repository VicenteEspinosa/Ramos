from backend_app.db_models.technician import Technician
from rest_framework import serializers


class TechnicianSerializer(serializers.ModelSerializer):
    """Technician serializer."""
    class Meta:
        """Meta."""

        model = Technician
        fields = (
            "id",
            "first_name",
            "last_name",
            "rut", 
            "enterprise_id",
            "phone",
            "email",
            "team_group_id",
            "category_id",
            "last_audit_date"
        )
