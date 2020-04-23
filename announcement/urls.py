from django.urls import path, include
from announcement import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('view_announcement/', views.viewAnnounce, name='view_announcement'),
    path('add_announcement/', views.announce, name='add_announcement'),
    path('edit_announcement/<int:announcement_id>', views.editAnnounce, name='edit_announcement'),
    path('delete_announcement/<int:announcement_id>', views.deleteAnnounce, name='delete_announcement'),
    path('getAnnounceJSON/', views.getAnnounceJSON, name='getAnnounceJSON')
]