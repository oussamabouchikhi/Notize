from django.conf.urls import url
# import views from this same folder
from . import views

app_name = 'note_app'
urlpatterns = [
    # http://127.0.0.1:8000/
    url(r'^$', views.allnotes, name='all_notes'),

]
