from rest_framework import serializers

from iotapi.models import User, IdentificationType, Coordinator, VehicleType, Vehicle, Driver, Assignment, Passenger


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
    
    class Meta:
        model = Vehicle
        fields = ['number_vehicle', 'vehicle_type',
                  'vehicle_status', 'license_plate']

# Driver
class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Driver
        fields = ['user', 'company_card', 'drivers_license', 'drivers_license_state']
        
# assignmanet
class AssignmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assignment
        fields = ['user', 'vehicle', 'Driver', 'state']
        
# passenger
class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ['user', 'passenger_code', 'passenger_permit']