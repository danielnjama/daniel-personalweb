from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post#, Comment
from django.views.generic import ListView
from .forms import  CommentForm
from django.http import HttpResponseRedirect

from django.db.models import Count
from django.contrib.auth.models import User




class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'


def post_detail(request, year, month, day, post):
    post=get_object_or_404(Post, slug=post,
                                 status='published',
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day
                                 )
    # return render(request,'blog/post_detail.html', {'post':post})

    # List of active comments for this post
    
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        #A comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            #create a Comment object but don't save to the database yet
            new_comment = comment_form.save(commit=False)
            #Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            #save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

        
    return  render(request, 'blog/post_detail.html', {'post':post,
                                                      'comments':comments,
                                                      'comment_form':comment_form,
                                                      
                                                      })



