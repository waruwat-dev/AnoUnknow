from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from chat.api import MessageModelViewSet
from chat import views

router = DefaultRouter()
router.register('message', MessageModelViewSet, basename='message-api')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]