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

class Image(models.Model):
 title = models.TextField()
 created_at = models.DateTimeField(auto_now_add=True)
 image = models.ImageField(upload_to='images/')

 def __str__(self):
   return self.title

class Comment(models.Model):
  comment_author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
  text = models.CharField(max_length=500, null=True)

  def __str__(self):
   return self.text



class Posts(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  post_category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
  post_author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
  post_body = models.CharField(max_length=2000, null=True)
  post_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, default=None)
  reactions = models.ManyToManyField(ReactionCategory, default=None)
  comments = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.category