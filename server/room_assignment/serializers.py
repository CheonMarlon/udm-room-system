from rest_framework import serializers
from .models import RoomAssignment

class RoomAssignmentSerializer(serializers.ModelSerializer):
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

