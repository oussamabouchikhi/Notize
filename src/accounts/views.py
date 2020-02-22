from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import UserForm, ProfileForm


def home(request):
    pass


def register(request):
    # form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # get username & password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            # redirect user to homePage(notes) after signup
            return redirect('/notes')

    else:
        # if error show registration form again
        form = UserCreationForm

    context = {
        'form': form,
    }
    
    return render(request, 'signup.html', context)   

# user profile
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile': profile}
    return render(request, 'profile.html', context)


# edit user profile
def edit_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        # if user submitted his profile edits(changes)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
    else:
        # if user didn't edit his profile yet
        # (instance=request.user) show user info in fields
        # request.FILES for image (files)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # new_profile = profile_form.save()
            # new_profile.user = request.user
            # new_profile.save()
            return redirect('/')


    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'edit_profile.html', context)


def change_password(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        # if user submitted his password edits(changes)
        password_form = PasswordChangeForm(request.user, request.POST)
        
    else:
        # if user didn't edit his password yet
        password_form = PasswordChangeForm(request.user)
        if password_form.is_valid():
            password_form.save()

    context = {
        'password_form': password_form,
        'profile': profile,
    }
    return render(request, 'change_password.html', context)
