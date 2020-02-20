from django.conf.urls import url
# import views from this same folder
from . import views

app_name = 'note_app'
urlpatterns = [
    # from views all_notes() function
    # http://127.0.0.1:8000/notes/
    url(r'^$', views.all_notes, name='all_notes'),
    
    # url(r'^(?P<id>\d+)$', views.detail, name='note_detail')
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='note_detail'),

    # http://127.0.0.1:8000/notes/add/
    url(r'^add$', views.note_add, name='add_note'),
    
    # http://127.0.0.1:8000/notes/edit/
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit')
]
