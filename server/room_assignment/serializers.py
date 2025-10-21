from rest_framework import serializers
from .models import RoomAssignment
from user_auth.models import CustomUser

class ProfessorSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['professor_id', 'full_name']

class RegisterProfessorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['professor_id', 'full_name', 'email', 'password']

    def create(self, validated_data):
        return

class RoomAssignmentSerializer(serializers.ModelSerializer):
    professor = ProfessorSummarySerializer(read_only=True)
    class Meta:
        model = RoomAssignment
        fields = [
            'id',
            'subject_code',
            'subject_name',
            'professor',
            'course_section',
            'room',
            'schedule_start',
            'schedule_end',
            'created_at',
            'status',  
        ]
        read_only_fields = ['id', 'created_at', 'professor']

