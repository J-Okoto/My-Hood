from rest_framework import serializers
from .models import neighbourhood


class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = neighbourhood
        fields = ('neighbourhood',)
        