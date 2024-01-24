from django.urls import path

from apps.users.views import (user_login, user_logout, members)

urlpatterns = [
    # User Authentication URLS
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    ## Members URLS
    path("members/", members, name="members"),
]