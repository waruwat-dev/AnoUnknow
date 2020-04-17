from django.urls import path, include
from announcement import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('view_announcement/', views.viewAnnounce, name='view_announcement'),
    path('add_announcement/', views.announce, name='announce'),
    path('edit_announcement/', views.editAnnounce, name='edit_announcement'),
    path('delete_announcement/', views.deleteAnnounce, name='delete_announcement'),
    
]