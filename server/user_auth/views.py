from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterProfessorSerializer

@api_view(['POST'])
def register_professor_api(request):
    serializer = RegisterProfessorSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message": "Professor registered successfully.",
            "professor_id": user.professor_id,
            "full_name": user.full_name,
            "email": user.email
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

