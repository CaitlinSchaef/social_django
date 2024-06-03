from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.TextField()
  last_name = models.TextField()

  def __str__(self):
    return self.user.username
  

class PostCategory(models.Model):
  category = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.category

class ReactionCategory(models.Model):
  reaction = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.reaction

class Image

class Comment

class Posts(models.Model):
  created_on = models.DateTimeField(default=timezone.now)
  post_category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
  post_author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
  reactions = models.ManyToManyField(ReactionCategory, on_delete=models.SET_NULL, null=True, default=blank)

  def __str__(self):
    return self.category