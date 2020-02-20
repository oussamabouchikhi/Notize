from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# show all notes
def all_notes(request):
    # return HttpResponse('<h1>Welcome to Django with Oussama</h1>')
    all_notes = Note.objects.all() # get all Note objects
    context = {  
        'all_notes': all_notes
    }
    return render(request, 'notes.html', context)

# show one note details
# replaced id with slug
def detail(request, slug):
    note = Note.objects.get(slug=slug)
    context = {
        'note' : note
    }
    return render(request, 'one_note.html', context)

# add a new note
def note_add(request):
    
    # if the request method is post
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            # create instance from form & prevent saving
            new_form = form.save(commit=False) 
            new_form.user = request.user # add user
            new_form.save()  # save the form
            messages.success(request, 'Note Created Sucessfully')#show success message
            return redirect('/notes') # redirect to home
    else:
        form = NoteForm()
    context = {
        'form' : form
    }
    return render(request, 'add.html', context)

# edit a note
def edit(request, slug):
    # get note details according to its slug
    note = get_object_or_404(Note, slug=slug)

    # if the request method is post
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            # create instance from form & prevent saving
            new_form = form.save(commit=False)
            new_form.user = request.user  # add user
            new_form.save()  # save the form
            # show success message
            messages.success(request, 'Note Edited Sucessfully')
            return redirect('/notes')  # redirect to home
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)