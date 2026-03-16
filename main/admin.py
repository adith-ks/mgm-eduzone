from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'semester', 'module', 'department', 'file')

admin.site.register(Note, NoteAdmin)