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
    model = PostCategory
    fields = ['category']

class PostSubCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = PostSubCategory
    fields= ['category', 'post_sub_category']


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
  class Meta:
    model = Posts
    fields = '__all__'
