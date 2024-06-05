from django.contrib import admin
from app_social.models import *


class ProfileAdmin(admin.ModelAdmin):
  pass

#anything you want to be able to manage/manipulate in the admin site needs to be established here

class PostCategoryAdmin(admin.ModelAdmin):
  pass

class PostSubCategoryAdmin(admin.ModelAdmin):
  pass

class ReactionCategoryAdmin(admin.ModelAdmin):
  pass

admin.site.register(ReactionCategory, ReactionCategoryAdmin)
admin.site.register(PostSubCategory, PostSubCategoryAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Profile, ProfileAdmin)

