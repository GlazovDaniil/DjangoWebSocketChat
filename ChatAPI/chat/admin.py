from django.contrib import admin
from .models import Conversation, Message


@admin.register(Conversation)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class ModelNameAdmin(admin.ModelAdmin):
    pass
