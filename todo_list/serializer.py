from rest_framework import serializers
from .models import ToDo




class ToDo_Serializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields='__all__'