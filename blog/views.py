from django.shortcuts import render

posts = [
    {
        'author': 'Nikolay',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 30, 2023',
    },
    {
        'author': 'Yana',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 31, 2023',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
