from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serial_json import MessageSerializer

@api_view(["POST"])
def send_message(request):
    user = request.data.get("user")
    question = request.data.get("message")

    if user == "A":
        response_text = "Usuário A, obrigado pelo contato!"
    else:
        response_text = "Usuário B, sua mensagem foi recebida!"

    message = Message.objects.create(
        user=user,
        question=question,
        response=response_text
    )

    return Response({
        "user": user,
        "question": question,
        "response": response_text
    })

@api_view(["GET"])
def get_history(request, user_id):
    messages = Message.objects.filter(user=user_id).order_by("created_at")
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
