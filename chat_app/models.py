from django.db import models

from chat_app.models import User

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_id")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver_id"
    )
    message = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
