from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^posts', views.post_list, name="posts"),
    url(r'^comments', views.comment_list, name="comments"),
    url(r'^posts', views.PostList.as_view(), name="posts"),
]
