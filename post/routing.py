from django.urls import re_path
# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
# ]
from django.conf.urls import url
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/post/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]