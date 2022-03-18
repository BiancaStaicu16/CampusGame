from django.contrib import admin
from api.gamemode.models import GameMode


class GameModeAdmin(admin.ModelAdmin):
    search_fields = ["users"]
    list_filter = ["created_at"]
    list_display = [
        "users",
        "cards"
    ]
    fields = [
        "users",
        "cards",
    ]
    readonly_fields = ["users", "cards"]

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(GameMode)
