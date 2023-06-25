from django.urls import path

from chat_app import views

app_name = "chat_app"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("dashboard/<str:room_name>/", views.DashboardView.as_view(), name="dashboard"),
]
