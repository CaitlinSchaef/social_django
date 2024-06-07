from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  # adding a serializer from user to profile
  user = UserSerializer()

  class Meta:
    model = Profile
    fields = ['id', 'first_name', 'last_name', 'user']


class PostCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = PostCategory
    fields = ['category']

class PostSubCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = PostSubCategory
    fields= ['post_sub_category']


class ReactionCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ReactionCategory
    fields = ['id', 'reaction_type']

class ReactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reaction
    fields = ['id', 'reaction', 'reaction_author']

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'comment_author', 'text']

class PostSerializer(serializers.ModelSerializer):
  post_author = ProfileSerializer(read_only=True)
  post_category = PostCategorySerializer(read_only=True)
  post_sub_category = PostSubCategorySerializer(read_only=True)
  
  class Meta:
    model = Posts
    fields = '__all__'
