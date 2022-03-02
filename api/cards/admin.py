from django.contrib import admin
from api.cards.models import Card


class CardAdmin(admin.ModelAdmin):
    """
    Different fields in the model and some
    of their properties
    """
    search_fields = ["title"]
    list_display = [
        "title",
        "value",
        "picture",
    ]
    fields = [
        "title",
        "value",
        "picture",
    ]


admin.site.register(Card, CardAdmin)
