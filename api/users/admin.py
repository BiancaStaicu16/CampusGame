from django.contrib import admin
from api.users.models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ["id"]
    list_filter = ["created_at"]
    list_display = [
        "id",
        "created_at",
    ]
    fields = [
        "id",
        "name",
        "username",
        "phone_number",
        "email",
        "cards",
        "is_verified",
        "is_staff",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["created_at", "updated_at", "id"]

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(User, UserAdmin)
