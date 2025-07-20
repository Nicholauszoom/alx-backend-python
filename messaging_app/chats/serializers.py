from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # explicitly using CharField

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'role']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    content = serializers.CharField()  # explicitly using CharField

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'content', 'timestamp']


class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True, source='message_set')
    message_count = serializers.SerializerMethodField()  # added SerializerMethodField

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'users', 'created_at', 'messages', 'message_count']

    def get_message_count(self, obj):
        return obj.message_set.count()


# Example of custom serializer with ValidationError
class CreateMessageSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    class Meta:
        model = Message
        fields = ['conversation', 'content']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message content cannot be empty or whitespace.")
        return value
