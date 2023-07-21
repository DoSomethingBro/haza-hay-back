from rest_framework import serializers
from Haza.models import User

class HazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
