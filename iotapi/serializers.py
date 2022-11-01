from rest_framework import serializers

from iotapi.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['identification_type', 'identification', 'phone', 'address', 'first_name', 'last_name']
