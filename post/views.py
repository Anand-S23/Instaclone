from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from user_activity.models import Act

# Create your views here.
@login_required
def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all().filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.comment_user = request.user
            instance.post = post
            instance.save()
            return HttpResponseRedirect(request.path_info)
    form = CommentForm()

    context={
        'post':post, 
        'comments':comments,
        'form':form
    }

    return render(request=request,
                  template_name='post/post.html',
                  context=context)

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(f'/user/{request.user}')
    form = PostForm()

    return render(request=request,
                    template_name='post/new_post.html',
                    context={
                        'form':form
                    })

class LikeSys(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user
        act = Act(to_user=post.user, from_user=user, act='liked')
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
            act.save()
        
        return reverse('post:view_post', kwargs={'pk':pk})
    
class OutLikeSys(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
            act = Act(to_user=post.user, from_user=user, act='liked')
        
        return reverse('home:home')
