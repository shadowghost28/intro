from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy
# estas son las Vista.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context={
            'posts':posts

        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form

        }
        return render(request, 'blog_create.html', context)   

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')


        context={

        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
     def post(self, request, pk,*args, **kwargs):
         post = get_object_or_404(Post, pk=pk)
         context={
             'post':post

         }
         return render(request, 'blog_Detail.html', context)

class BlogUpdateView(UpdateView):
    model=Post
    fields=['title','content']
    templates_name='blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})