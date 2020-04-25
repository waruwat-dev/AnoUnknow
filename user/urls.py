from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.api import UserModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet, basename='user-api')
from . import views

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', views.main, name='main'),
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('user_list/', views.user_list, name='user_list'),
    path('ban_list/', views.ban_list, name='ban_list'),
    path('ban/<int:user_id>/', views.ban_use, name='ban'),
    path('changepassword/', views.changePassword, name='changePassword'),
]

