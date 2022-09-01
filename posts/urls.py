from django.urls import path
from posts.views import PostsListView,PostDetailView

urlpatterns = [
    path('', PostsListView.as_view(), name = 'posts_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
]