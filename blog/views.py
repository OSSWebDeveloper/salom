from django.shortcuts import render,  redirect 
from .models import *
from django.db.models import Q
from .forms import *
from django.urls import reverse
# Create your views here.



def index (request):
    posts = Post.objects.order_by('-date')[:6]
    return render(request, 'blog/index.html', {'posts':posts})


def search(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(title__icontains=query) 
    )
    return render(request, 'blog/search.html', {'search_obj':search_obj, 'query':query})


def posts(request):
    posts = Post.objects.all()
    return render(request , 'blog/posts.html', {'posts':posts})


def post(request,id):
    post = Post.objects.get(id=id)
    post.views += 1
    post.save()
    return render(request , 'blog/post.html', {'post':post})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories':categories})

def category(request,id):
    category = Category.objects.get(id=id)
    posts = Post.objects.filter(categories=category).order_by("-date")
    return render(request, 'blog/category.html', {'category':category, 'posts':posts})




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})


def comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = post.comment_set.create(
       
            text = request.POST.get('text')
        )
        if request.user.is_superuser:
            comment.publish = True
            comment.save()
            return redirect('index')
    return redirect(reverse('post.html', kwargs={'id': id}))



