from django.shortcuts import render
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'Amira Ben Said ',
        'title': 'Blog Post 1',
        'content':'this is my first blog post',
        'date_posted':'7th April, 2024'
    },
    {
        'author': 'Manar Dhrif ',
        'title': 'Blog Post 2',
        'content':'this is my second blog post',
        'date_posted':'14th April, 2024'
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request , 'blog/home.html', context)

#View needs url in django

def about(request):
    return render(request , 'blog/about.html')