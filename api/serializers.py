from rest_framework import serializers
from core.models import ToDo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'body',
        )
        model = ToDo
