from rest_framework import serializers

from iotapi.models import User, IdentificationType, Coordinator, VehicleType, Vehicle


class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    identification_type_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['identification_type', 'identification_type_name', 'identification',
                  'phone', 'address', 'email', 'first_name', 'last_name', 'password', 'username']

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance

    def update(self, instance, validated_data):
        return super(UserSerializer, self).update(instance, validated_data)


class CoordinatorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Coordinator
        fields = ['user']


class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleType
        fields = ['name', 'description']


class VehicleSerializer(serializers.ModelSerializer):
    VehicleType = VehicleTypeSerializer()

    class Meta:
        model = Vehicle
        fields = ['id_vehicle', 'vehicle_type',
                  'vehicle_status', 'license_plate']
