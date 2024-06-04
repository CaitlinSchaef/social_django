from django.contrib import admin
from app_social.models import *


class ProfileAdmin(admin.ModelAdmin):
  pass

#anything you want to be able to manage/manipulate in the admin site needs to be established here




admin.site.register(Profile, ProfileAdmin)
