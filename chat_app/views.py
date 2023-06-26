from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from chat_app.models import Message
from core.models import User


class HomeView(TemplateView):
    template_name = "chat_app/home.html"


class DashboardView(LoginRequiredMixin, View):
    login_url = "core:login"

    def get(self, request, room_name=None):
        user = request.user
        sender_id = user.id
        loggedin_user_email = user.email
        users = User.objects.all().exclude(email=loggedin_user_email)

        if not room_name:
            context = {
                "users": users,
                "sender_id": sender_id,
            }
            return render(request, "chat_app/dashboard.html", context=context)

        receiver_id = request.GET.get("receiver")
        receiver = User.objects.get(id=receiver_id)
        receiver_id = receiver.id
        messages = Message.objects.filter(
            Q(Q(sender=sender_id) & Q(receiver=receiver_id))
            | Q(Q(sender=receiver_id) & Q(receiver=sender_id))
        ).order_by("created_at")

        context = {
            "users": users,
            "room_name": room_name,
            "receiver_id": receiver_id,
            "sender_id": sender_id,
            "messages": messages,
            "receiver_name": receiver.name,
            "room_name": room_name,
        }
        return render(request, "chat_app/dashboard.html", context)
