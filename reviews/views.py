from django.shortcuts import render, redirect
from reviews.models import Post, Comment
from reviews.forms import PostForm, CommentForm
# from accounts.models import


def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    return render(request, 'list.html', {'reviews': my_list})


def p_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('reviews:list')

    return render(request, 'create.html')
