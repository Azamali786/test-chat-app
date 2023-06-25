from django.contrib import admin

from chat_app.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "gender",
        "date_of_birth",
        "contact_number",
        "is_available",
        "created_at",
    )


admin.site.register(User, UserAdmin)
