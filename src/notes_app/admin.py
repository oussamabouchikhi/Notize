from django.contrib import admin

# Register your models here.

''' 
import Note models which is in the same directory (.)
'''
from .models import Note

#? This customazation is specially for notes_app each app could to be customized from its admin.py file 
class AdminNotes(admin.ModelAdmin):
    # use Note model attributes from ./models to filter notes
    list_filter = ['user', 'tags', 'created'] # filter by user, tags, created date
    list_display = ['title', 'created', 'active'] # information to display for each note
    search_fields = ['title', 'content'] # search by title in searchField


# Add the model to admin panel
admin.site.register(Note, AdminNotes)
