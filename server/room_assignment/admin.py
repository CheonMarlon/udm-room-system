from django.contrib import admin
from .models import RoomAssignment

@admin.register(RoomAssignment)
class RoomAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'subject_code',
        'subject_name',
        'professor',
        'course_section',
        'room',
        'schedule_start',
        'schedule_end'
    ]
    list_filter = ['professor', 'room', 'schedule_start']
    search_fields = ['subject_code', 'subject_name', 'course_section', 'room']
    raw_id_fields = ['professor']
    date_hierarchy = 'schedule_start'
    ordering = ['schedule_start']
    

