from django.urls import path, include
from comment import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('addComment/<int:pk>', views.addComment, name='addComment'),
    path('emotion/<int:pk>/<int:type_emotion>', views.emotionComment, name='emotion_comment'),
    path('getcomment/<int:pk>', views.getComment, name='getComment'),
]