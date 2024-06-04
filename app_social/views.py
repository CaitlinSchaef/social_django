from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

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
# Posts (images framework)

#Create New Post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# the parser helps it read data
@parser_classes([MultiPartParser, FormParser])
def create_posts(request):
  # serialize the image that the user is submitting by running it through the image serializer
  post_serialized = PostSerializer(data=request.data)
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

#Update Post
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_post(request):
  user = request.user

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


#########################################################################################################################################################################################
#Reactions 

