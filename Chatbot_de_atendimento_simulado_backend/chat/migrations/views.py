from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, MOCK_RESPONSES
from .serializers import MessageSerializer
from django.db import transaction 

class ChatBotView(APIView): 

    def post(self, request, *args, **kwargs): 

        user_profile = request.data.get('user_profile')
        user_text = reques.data.get('text')

        if user_profile not in ['A', 'B']:
            return Response({'error': 'Perfil de usuário inválido.'}, status=status.HTTP_400_BAD_REQUEST) 
        
        if not user_text: 
            return Response({"error": "O campo 'text' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            user_message = Message.objects.create(
                user_profile = user_profile,
                sender = user_profile,  
                text = user_text
            )

            backend_response_text = MOCK_RESPONSES.get(user_profile, "Obrigado por entrar em contato. Retornaremos em breve.")

            backend_message = Message.objects.create(
                user_profile = user_profile,
                sender = 'Backend',  
                text = backend_response_text
            )

        serializer = MessageSerializer(backend_message)

        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
class HistoryView(APIView): 

    def get(self, request, *args, **kwargs):
        if user_profile not in ['A', 'B']:
            return Response({'error': 'Perfil de usuário inválido.'}, status=status.HTTP_400_BAD_REQUEST) 
        
        messages = Message.objects.filter(user_profile=user_profile) 

        serializer = MessageSerializer(messages, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)