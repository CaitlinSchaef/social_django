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

class PostSubCategory(models.Model):
  post_sub_category = models.CharField(max_length=100, null=True)

  def __str__(self):
    return f'ID: {self.id} SubCategory: {self.post_sub_category}'

class ReactionCategory(models.Model):
  reaction_type = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.reaction_type

class Reaction(models.Model):
  reaction = models.ForeignKey(ReactionCategory, on_delete=models.CASCADE)
  reaction_author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.reaction


class Comment(models.Model):
  comment_author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
  text = models.CharField(max_length=500, null=True)

  def __str__(self):
   return f'{self.text} by: {self.comment_author}'


class Posts(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  post_category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
  post_sub_category = models.ForeignKey(PostSubCategory, on_delete=models.SET_NULL, null=True)
  post_author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
  post_body = models.CharField(max_length=2000, null=True)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  image_caption = models.TextField(null=True, blank=True)
  reactions = models.ForeignKey(Reaction, on_delete=models.SET_NULL, null=True)
  comments = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f'Category: {self.post_category}, Author: {self.post_author}, {self.post_body} {self.image} {self.image_caption}, Posted: {self.created_on} {self.comments} {self.reactions}'