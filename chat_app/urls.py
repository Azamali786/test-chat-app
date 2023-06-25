from django.urls import path
from chat_app import views

app_name = "chat_app"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home")
]