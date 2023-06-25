import json

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat_app.models import Message, User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        user = self.scope["user"]
        text_data_json = json.loads(text_data)
        sender_id = user.id
        receiver_id = text_data_json.get("receiver_id")
        message = text_data_json["message"]
        message = message  # add to message here

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender_id": sender_id,
                "receiver_id": receiver_id,
            },
        )

    # Receive message from room group
    async def chat_message(self, event, **kwargs):
        sender_id = event.get("sender_id")
        receiver_id = event.get("receiver_id")
        message = event["message"]

        await database_sync_to_async(Message.objects.get_or_create)(
            sender=await sync_to_async(User.objects.filter(id=sender_id).first)(),
            receiver=await sync_to_async(User.objects.filter(id=receiver_id).first)(),
            message=message,
        )

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                }
            )
        )
