from .views import (ArticleListView, ArticleDetailView,
                    ArticleCreateView, ArticleUpdateView, ArticleDeleteView)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete')
]
