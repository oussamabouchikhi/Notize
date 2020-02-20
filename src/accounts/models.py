from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime
from django.db.models.signals import post_save


class Profile(models.Model):
    # every user has one profile linked to it
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(blank=True, max_length=100)
    # last_name = models.CharField(blank=True, max_length=100)
    slug = models.CharField(blank=True, null=True, max_length=100)
    headline = models.CharField(blank=True, max_length=100)
    bio = models.TextField(blank=True)
    img = models.ImageField(upload_to="profile_img")
    join_date = models.DateTimeField(blank=True, default=datetime.datetime.now)

    # function to save this profile
    def save(self, *args, **kwargs):
        # if this profile has no slug
        if not self.slug:
            # generate a slug from profile user(username) (before saving)
            self.slug = slugify(self.user)
        # Override save method 
        super(Profile, self).save(*args, **kwargs)

    # show user profile
    def __str__(self):
        return '{}'.format(self.user)
        
### Signals
# When a user creates an account his
# profile should be created automatically
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)         
