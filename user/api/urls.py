from django.urls import path
from user.api.views import UserDetailsAPIView, UserListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("edit-delete-get-user/<int:user_id>/", UserDetailsAPIView.as_view(), name="user-detail"),
]