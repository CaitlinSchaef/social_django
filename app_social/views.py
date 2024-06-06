from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework import viewsets

from .models import *
from .serializers import *

#########################################################################################################################################################################################
# Users
#Get Users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
  user = request.user
  profile = user.profile
  serializer = ProfileSerializer(profile, many=False)
  return Response(serializer.data)

#Create New User
@api_view(['POST'])
@permission_classes([])
def create_user(request):
   user = User.objects.create(
       username = request.data['username'],
   )
   user.set_password(request.data['password'])
   user.save()
   profile = Profile.objects.create(
       user = user,
       first_name = request.data['first_name'],
       last_name = request.data['last_name']
   )
   profile.save()
   profile_serialized = ProfileSerializer(profile)
   return Response(profile_serialized.data)

#########################################################################################################################################################################################
# Posts (images included so utilizing the parsers)

#Create New Post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# the parser helps it read data
@parser_classes([MultiPartParser, FormParser])
def create_posts(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  post_author = profile.id
  # serialize the image that the user is submitting by running it through the image serializer
  # you're gonna need to set the back end to default the image as 'null'?
  post_data = {
    'post_author': post_author,
    'post_body': request.data['post_body'],
    'post_category': request.data['post_category'],
    'post_sub_category': request.data['post_sub_category'],
    'image': request.data['image'],
    'image_caption': request.data['image_caption'],
  }
  post_serialized = PostSerializer(data=post_data)
  print('POST SERIALIZED: ', post_serialized)
  # then check to see if it's valid, this is a django built in (the is_valid())
  if post_serialized.is_valid():
    post_serialized.save()
    # when you return a response you're giving a response back to your user
    # Response is a rest framework that we imported at the top
    # jason is going to send back the status and the image
    return Response(post_serialized.data, status=status.HTTP_201_CREATED)
  return Response(post_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#Get Posts
@api_view(['GET'])
@permission_classes([IsAuthenticated])
# isAuthenticated is something we imported, we could also do IsAdmin or allowAny, it's gonna looks for the JWT for the user
def get_posts(request):
  posts = Posts.objects.all()
  # default is many=False, which would just serialize one object, this will return a whole list
  posts_serialized = PostSerializer(posts, many=True)
  return Response(posts_serialized.data)

#Update Post body? do i need to do one for image?
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_post(request):
  user = request.user
  id = request.data['id']
  posts = Posts.objects.get(pk=id)

  posts.post_body = request.data['post_body']
  posts.save()

  posts_serialized = PostSerializer(posts)
  return Response(posts_serialized.data)

#Delete Post?

#########################################################################################################################################################################################
#Comments

#Get Comments
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request):
  comments = Comment.objects.all()
  # default is many=False, which would just serialize one object, this will return a whole list
  comments_serialized = CommentSerializer(comments, many=True)
  return Response(comments_serialized.data)

#Create New Comment
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# the parser helps it read data
@parser_classes([MultiPartParser, FormParser])
def create_comment(request):
  # serialize the image that the user is submitting by running it through the image serializer
  comment_serialized = CommentSerializer(data=request.data)
  # then check to see if it's valid, this is a django built in (the is_valid())
  if comment_serialized.is_valid():
    comment_serialized.save()
    # when you return a response you're giving a response back to your user
    # Response is a rest framework that we imported at the top
    # jason is going to send back the status and the image
    return Response(comment_serialized.data, status=status.HTTP_201_CREATED)
  return Response(comment_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#Edit Comment

#Delete Comment

#########################################################################################################################################################################################
#Reactions

#Get Reactions

#Create Reactions

#Edit Reactions

#Delete Reactions

#########################################################################################################################################################################################
# class views for back end

class ReactionCategoryViewSet(viewsets.ModelViewSet):
  queryset = ReactionCategory.objects.all()
  serializer_class = ReactionCategorySerializer

class PostCategoryViewSet(viewsets.ModelViewSet):
  queryset = PostCategory.objects.all()
  serializer_class = PostCategorySerializer

class PostSubCategoryViewSet(viewsets.ModelViewSet):
  queryset = PostSubCategory.objects.all()
  serializer_class = PostSubCategorySerializer

