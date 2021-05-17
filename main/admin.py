from django.contrib import admin
from .models import ForUser, Jeunes,University,NotesUniversity,NotesJeunes
admin.site.register(University),
admin.site.register(NotesUniversity),
admin.site.register(Jeunes),
admin.site.register(NotesJeunes)
