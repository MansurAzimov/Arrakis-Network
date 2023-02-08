from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect
from posts.models import Post,Comment

class PostsListView(ListView):
    model = Post
    template_name ='posts/index.html'
    context_object_name = 'posts'

class PostDetailView (DetailView):
    model = Post
    template_name ='posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    fields = ('title','body',)
    
    def post(self, requset, *args,**kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return redirect ('posts_list')

def add_comment(request):
    message = request.POST.form.get('message')
    comment = Comment(message=message, author=request.user)
    comment.save()
    return request ('posts_detail')

class PostUpdateView(UpdateView):
    model = Post
    template_name ='posts/post_update.html'

    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    success_url='/'
    template_name ='posts/post_delete.html'

