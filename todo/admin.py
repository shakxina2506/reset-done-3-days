from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('task', 'description', 'deadline', 'updated_at')