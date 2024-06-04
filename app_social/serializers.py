from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'first_name', 'last_name']


class PostCategorySerializer(serializers.ModelSerializer):
  class Meta:
    models = PostCategory
    fields = ['category']

class ReactionCategorySerializer(serializers.ModelSerializer):
  class Meta:
    models = ReactionCategory
    fields = ['id', 'reaction', 'reaction_author']

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    models = Comment
    fields = ['id', 'comment_author', 'text']

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    models = Posts
    fields = '__all__'
