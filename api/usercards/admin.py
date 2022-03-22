from django.contrib import admin
from api.usercards.models import UserCard


class UserCardAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    list_filter = ["created_at"]
    list_display = ["user", "card"]
    fields = [
        "user",
        "card",
    ]
    readonly_fields = ["user", "card"]

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(UserCard)
