from django.contrib import admin

from chat_app.models import Message


class MessaageAdmin(admin.ModelAdmin):
    list_display = ("receiver_id", "sender_id", "message", "created_at")


admin.site.register(Message, MessaageAdmin)
