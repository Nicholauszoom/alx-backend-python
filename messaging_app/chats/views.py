from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Conversation, Message, User
from .serializers import (
    ConversationSerializer,
    MessageSerializer,
    CreateMessageSerializer,
)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_ids = request.data.get("user_ids")
        if not user_ids or len(user_ids) < 2:
            return Response(
                {"detail": "At least two users are required to start a conversation."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users = User.objects.filter(user_id__in=user_ids)
        if users.count() < 2:
            return Response(
                {"detail": "Some user IDs are invalid."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        conversation = Conversation.objects.create()
        conversation.users.set(users)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMessageSerializer
        return MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        conversation = get_object_or_404(Conversation, pk=request.data['conversation'])
        message = Message.objects.create(
            sender=request.user,
            conversation=conversation,
            content=serializer.validated_data['content']
        )
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

