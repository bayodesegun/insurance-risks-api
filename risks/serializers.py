from rest_framework import serializers
from .models import Risk

class RiskDataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Risk

    def to_representation(self, obj):
       	return obj.get_data()

class RiskListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Risk
        fields = ('id', 'name',)
