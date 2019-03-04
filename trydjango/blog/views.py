from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
