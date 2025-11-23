from rest_framework import serializers 
from .models import Message 

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'users_pro', 'sender', 'text', 'timestamp'] 
        read_only_fields = ['id', 'timestamp', 'sender']