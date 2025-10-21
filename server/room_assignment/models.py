from django.db import models
from django.conf import settings
from django.utils import timezone

# Room assignment model 
class RoomAssignment(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    ]
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='room_assignments'
    )
    course_section = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    schedule_start = models.DateTimeField()
    schedule_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # metadata order, the order starts from schedule_start 
    class Meta:
        ordering = ['schedule_start']
        indexes = [
            models.Index(fields=['schedule_start']),
        ]

    def __str__(self):
        return f"{self.subject_code} - {self.course_section} in {self.room} by {self.professor}"

    def get_absolute_url(self):
        return reverse('room_assignment:detail', args=[str(self.id)])


