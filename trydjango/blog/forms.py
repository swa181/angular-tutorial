from .models import Article
from django import forms


class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("title", "description")
