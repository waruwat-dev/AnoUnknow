from django.urls import path, include
from post.api import PostViewSet
from comment import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('addComment/<int:pk>', views.addComment, name='addComment'),
]