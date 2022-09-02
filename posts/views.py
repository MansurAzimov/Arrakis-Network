from django.views.generic import ListView,DetailView

from posts.models import Post

class PostsListView(ListView):
    model = Post
    template_name ='index.html'
    context_object_name = 'posts'

class PostDetailView (DetailView):
    model = Post
    template_name ='post_detail.html'
    context_object_name = 'posts'