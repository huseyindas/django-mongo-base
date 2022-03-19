from django.urls import path

from apps.user.views import UserView


app_name = "user"
urlpatterns = [
    path("", UserView.as_view(), name="users"),
]
