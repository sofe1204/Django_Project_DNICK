from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import BlogPost, user, Commentar,Block
from .forms import BlogPostForm, BlockUserForm


# Create your views here.

def postsAdd(request):
    if request.method == "POST":
        form_data = BlogPostForm(data=request.POST)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts")

    context = {"form": BlogPostForm}
    return render(request, "PostForm.html", context=context)


def posts(request):
    queryset = BlogPost.objects.all()
    context = {"posts": queryset}
    return render(request, "posts.html", context=context)


@login_required()
def users(request):
    queryset1 = BlogPost.objects.filter(author=request.user).all()
    queryset2 = user.objects.filter(user=request.user).all()
    context = {"posts": queryset1, "users": queryset2, "form": BlockUserForm}
    return render(request, "profile.html", context=context)


def blockedUser(request):
    if request.method == "POST":
        form_data = BlockUserForm(data=request.POST)
        if form_data.is_valid():
            # user = form_data.save(commit=False)
            # user.user = request.user
            # user.save()
            return redirect("/profile")
    queryset = user.objects.filter(user=request.user).all()
    context = {"blocked_users": queryset, "form": BlockUserForm}
    return render(request, "blockedUsers.html", context=context)
