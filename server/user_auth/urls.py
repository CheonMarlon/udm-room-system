from django.urls import path
from .views import register_professor_api

urlpatterns = [
    path('register/', register_professor_api, name='register-professor'),
]

