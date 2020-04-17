from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.api import PostViewSet
from post import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls), name='post_api'),
    path('main_post/', views.view_all_posts, name='view_all_posts'),
    path('view_post/<int:pk>', views.view_post, name='view_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('emotion/<int:pk>/<int:type_emotion>', views.emotionPost, name='emotion_post')
]