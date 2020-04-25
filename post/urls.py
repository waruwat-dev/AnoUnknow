from django.urls import path, include
from post import views
from post import api

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/get_random_posts/', api.get_random_posts, name='get_random_posts'),
    path('api/get_post/<int:post_id>', api.get_post, name='get_post'),
    path('api/get_detail_post/<int:post_id>', api.get_detail_post, name='get_detail_post'),
    path('api/distribute_post/<int:post_id>', api.distribute_post, name='distribute_post'),
    path('api/get_hashtag', api.getHashtag, name="get_hashtag"),
    path('api/edit_post/', api.edit_post, name='edit_post'),
    path('view_all_posts/', views.view_all_posts, name='view_all_posts'),
    path('view_random_posts/', views.view_random_posts, name='view_random_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('emotion/<int:pk>/<int:type_emotion>', views.emotionPost, name='emotion_post'),
    path('view_hashtag/<word>', views.view_hashtag, name='view_hashtag')
]