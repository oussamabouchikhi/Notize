from django.shortcuts import render

# Create your views here.
from notes_app.models import Note


def allnotes(request):
    notes = Note.objects.all() # get all notes
    return render(request, 'home.html', {'all_notes': notes})