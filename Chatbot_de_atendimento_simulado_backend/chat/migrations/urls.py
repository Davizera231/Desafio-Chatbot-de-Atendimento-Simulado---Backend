from django.urls import path
from .views import ChatView, HistoryView

urlpatterns = [
    
    path('chat/', ChatView.as_view(), name='send_message'),
    
    path('history/<str:user_profile>/', HistoryView.as_view(), name='get_history'),
]