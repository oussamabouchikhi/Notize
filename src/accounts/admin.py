from django.contrib import admin

# Register your models here.
from .models import Profile

#? This customazation is specially for notes_app each app could to be customized from its admin.py file 
class AdminProfile(admin.ModelAdmin):
    # use Profile model attributes from ./models to filter user
    list_filter = ['headline', 'join_date'] # filter user by username, join date
    list_display = ['user', 'slug', 'headline', 'join_date'] # information to display for each user
    #? user is foreign key so we can't search with it
    # each user profile is related to a user and each user has first_name, last_name, email
    # so we can search like: user__attribute
    search_fields = ['user__first_name', 'slug','join_date'] # search by title in searchField
    list_editable = ['headline']
    #list_display_links = None # if there is an error with 'title' in list_editable

admin.site.register(Profile, AdminProfile)
