from django.urls import path

from apps.users.apis.views import MemberDebtAPIView
from apps.users.views import (delete_member, edit_member, members, new_member,
                              user_login, user_logout)

urlpatterns = [
    # User Authentication URLS
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    ## Members URLS
    path("members/", members, name="members"),
    path("new-member/", new_member, name="new-member"),
    path("edit-member/", edit_member, name="edit-member"),
    path("delete-member/", delete_member, name="delete-member"),
    path("member-debt/", MemberDebtAPIView.as_view(), name="member-debt"),
]