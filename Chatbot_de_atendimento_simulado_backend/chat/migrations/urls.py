from django.urls import path
from .views import send_message, get_history

urlpatterns = [
    path("send/", send_message),
    path("history/<str:user_id>/", get_history),
]
