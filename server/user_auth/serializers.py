from rest_framework import serializers
from .models import CustomUser

class RegisterProfessorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['professor_id', 'full_name', 'email', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

