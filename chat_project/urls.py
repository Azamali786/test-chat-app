from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("core/", include("core.urls", namespace="core_app")),
    path("chat/", include("chat_app.urls", namespace="chat_app")),
]
