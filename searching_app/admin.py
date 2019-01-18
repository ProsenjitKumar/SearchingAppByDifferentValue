from django.contrib import admin
from .models import Actor


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'age']


admin.site.register(Actor, ActorAdmin)
