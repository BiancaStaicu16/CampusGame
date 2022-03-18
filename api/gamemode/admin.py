#admin.py

from django.contrib import admin
from api.gameMode.models import GameMode


class GameModeAdmin(admin.ModelAdmin):
    search_fields = ["users"]
    list_filter = ["created_at"]
    list_display = [
        "users",
    ]
    fields = [
        "users",
    ]
    readonly_fields = ["users"]

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(GameMode)
