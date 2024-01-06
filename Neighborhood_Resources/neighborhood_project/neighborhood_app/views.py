from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from neighborhood_app.models import Post, Comment
from django.contrib.auth.decorators import login_required
from neighborhood_app.forms import PostForm, CommentForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'neighborhood_app/index.html')

class about(TemplateView):
    template_name = 'neighborhood_app/about.html'
    
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = Post
    
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'neighborhood_app:post_detail.html'   
    form_class = PostForm
    model = Post
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'neighborhood_app:post_detail.html'   
    form_class = PostForm
    model = Post
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('neighborhood_app:post_list')
    
class DraftListView(LoginRequiredMixin,ListView):
    context_object_name = 'draft_post'
    login_url = '/login/'
    template_name = 'neighborhood_app/post_draft_list.html'
    
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
    
    
#########################################################
#########################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('neighborhood_app:post_detail', pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if(form.is_valid()):
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('neighborhood_app:post_detail', pk=post.pk)
        
    else:
        form = CommentForm()
        
    return render(request, 'neighborhood_app/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('neighborhood_app:post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('neighborhood_app:post_detail', pk=post_pk)

######################################################### 
#########################################################
    
class team(TemplateView):
    template_name = 'neighborhood_app/team.html'

class credit(TemplateView):
    template_name = 'neighborhood_app/credits.html'
    
class jobs(TemplateView):
    template_name = 'neighborhood_app/jobs.html'
    
class faq(TemplateView):
    template_name = 'neighborhood_app/faq.html'