from django.urls import path
from . import views
urlpatterns = [
    path('rooms/', views.list_rooms_query_api, name='room-list'),
    path('rooms/create/', views.create_room_assignment_api, name='room-create'),
    path('rooms/delete/<int:assignment_id>/', views.delete_room_assignment_api, name='room-delete') 
]

