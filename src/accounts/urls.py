from django.conf.urls import url
# import views from this same folder
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'^$', views.home, name='home'),
    # login
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    # logout
    url(r'^logout$', LogoutView),
    # signup(register)
    url(r'^signup$', views.register, name='register'),

    # User Profile
    url(r'^(?P<slug>[-\w]+)/$', views.profile, name='profile'),
    # Edit User Profile
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit_profile, name='edit_profile'),

    url(r'^(?P<slug>[-\w]+)/change_password$',
        views.change_password, name='change_password')

]
