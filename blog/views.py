from django.shortcuts import render
from django.views.generic.base import View
from .forms import PostCreateForm
# estas son las Vista.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'blog_create.html', context)   

    def Post(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'blog_create.html', context)