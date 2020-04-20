from django.urls import path, include
from post import views
from post import api

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/post_list/', api.post_list, name='post_list'),
    path('api/distribute_post/<int:post_id>', api.distribute_post, name='distribute_post'),
    path('view_all_posts/', views.view_all_posts, name='view_all_posts'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('view_post/<int:pk>', views.view_post, name='view_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('emotion/<int:pk>/<int:type_emotion>', views.emotionPost, name='emotion_post')
]