from allauth.socialaccount import admin
from django.contrib import admin
from django.db import models
# Register your models here.
from chat.models import Chat, Volunteer, Nurse, Patient


@admin.register(Chat)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('message', 'created', 'user',)
    search_fields = ['message']


admin.site.register(Volunteer)
admin.site.register(Nurse)
admin.site.register(Patient)