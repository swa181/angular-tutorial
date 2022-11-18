from django.shortcuts import render
from django.urls import reverse
from .models import Article
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView)
from .forms import ArticleModelForm

# Create your views here.


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html

    def get_success_url(self) -> str:
        return reverse('blog:article-list')


# def article_list_view(request, id):
#     obj = get_object_or_404(Article, id=id)

#     context = {
#         "obj": obj
#     }

#     return render(request, "")
