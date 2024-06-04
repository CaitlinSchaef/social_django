from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from app_social.views import *
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post-category', PostCategoryViewSet)
router.register(r'post-subcategory', PostSubCategoryViewSet)
router.register(r'reaction-category', ReactionCategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('profile/', get_profile),
    path('posts', get_posts),
    path('create-post/', create_posts),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
]

# this is saying if debug = true (which it is)
if settings.DEBUG:
    from django.conf.urls.static import static
    # we're adding something to the url pattern to handle the images when we're in local development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
