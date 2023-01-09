from django.urls import path
from posts.views import PostsListView,PostDetailView,PostCreateView,add_comment

urlpatterns = [
    path('', PostsListView.as_view(), name = 'posts_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='new_post'),
    path('<int:pk>', PostDetailView.as_view(), name='add_comment')
]