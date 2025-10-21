from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import RoomAssignment
from .serializers import RoomAssignmentSerializer

# Create your views here.

ALLOWED_TAGS = ['Available', 'Reserved']

@api_view(['GET'])
def list_rooms_query_api(request):
    tag = request.GET.get('tag')
    assignments = RoomAssignment.objects.select_related('professor').order_by('-schedule_start')
    if tag:
        if tag not in ALLOWED_TAGS:
            return Response({"error": "Invalid tag filter."}, status=status.HTTP_400_BAD_REQUEST) 
        assignments = assignments.filter(status=tag)
    serializer = RoomAssignmentSerializer(assignments, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_room_assignment_api(request):
    serializer = RoomAssignmentSerializer(data=request.data)
    if serializer.isValid():
        serializer.save(professor=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_room_assignment_api(request, assignment_id):
    assignment = get_object_or_404(RoomAssignment, id=assignment_id)
    if request.user != assignment.professor and not request.user.is_superuser:
        return Response({"error": "Not allowed to delete this assignment."}, status=403)
    assignment.delete()
    return Response(status=204)

