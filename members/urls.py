# In members/urls.py
from django.conf.urls import url

from . import views

app_name = "members"
urlpatterns=[
  url(r'^$', views.AllMembersView.as_view(), name="all_members"),
  url(r'^new_member/$', views.NewMemberView.as_view(), name="new_member"),
]
