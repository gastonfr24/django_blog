from audioop import reverse
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import postCreateForm
from .models import post
from django.urls import reverse_lazy


class blogListView(View):
    def get(self, request, *args, **kwargs):
        posts = post.objects.all
        context = {
            'posts': posts
        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = postCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = postCreateForm(request.POST)
            if form.is_valid():
                tittle = form.cleaned_data.get('tittle')
                content = form.cleaned_data.get('content')

                p, created = post.objects.get_or_create(
                    tittle=tittle, content=content)
                p.save()
                return redirect('blog:home')
        context = {

        }
        return render(request, 'blog_create.html', context)


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        posta = get_object_or_404(post, pk=pk)
        context = {
            'post': posta
        }

        return render(request, 'blog_detail.html', context)


class BlogUpdateView(UpdateView):
    model = post
    fields = ['tittle', 'content']

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk': pk})


class BlogDeleteView(DeleteView):
    model = post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')
