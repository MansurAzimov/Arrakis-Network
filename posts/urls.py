from django.urls import path
from posts.views import PostsListView,PostDetailView,PostCreateView,add_comment,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostsListView.as_view(), name = 'posts_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='new_post'),
    path('<int:pk>', add_comment, name='add_comment'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]