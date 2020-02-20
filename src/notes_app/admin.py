from django.contrib import admin

# Register your models here.

''' 
import Note models which is in the same directory (.)
'''
from .models import Note

# Add the model to admin panel
admin.site.register(Note)
