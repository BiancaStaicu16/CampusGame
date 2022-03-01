from django.contrib import admin
from api.cards.models import Card


class CardAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["created_at"]
    list_display = [
        "id",
        "created_at",
    ]
    fields = [
        "title",
        "value",
        "picture",
    ]

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Card, CardAdmin)
