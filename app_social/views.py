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

#########################################################################################################################################################################################
# Images

#Create New Image
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# the parser helps it read data
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
  # serialize the image that the user is submitting by running it through the image serializer
  image_serialized = ImageSerializer(data=request.data)
  # then check to see if it's valid, this is a django built in (the is_valid())
  if image_serialized.is_valid():
    image_serialized.save()
    # when you return a response you're giving a response back to your user
    # Response is a rest framework that we imported at the top
    # jason is going to send back the status and the image
    return Response(image_serialized.data, status=status.HTTP_201_CREATED)
  return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#Get Images
@api_view(['GET'])
@permission_classes([IsAuthenticated])
# isAuthenticated is something we imported, we could also do IsAdmin or allowAny, it's gonna looks for the JWT for the user
def get_images(request):
  images = Image.objects.all()
  # default is many=False, which would just serialize one object, this will return a whole list
  images_serialized = ImageSerializer(images, many=True)
  return Response(images_serialized.data)

#########################################################################################################################################################################################
#Comments

#########################################################################################################################################################################################
#Reactions 

#########################################################################################################################################################################################
#Posts