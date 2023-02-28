from django import forms
from Article.models import Article, Message

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ["Title", "Content"]
    labels = {
      "Title"  : "Title",
      "Content": "Content",
    }
    widgets = {
      "Title"  : forms.TextInput(attrs={"class": "form-control"}),
      "Content": forms.Textarea(attrs={"class": "form-control"}),
    }

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ["Content"]
    labels = {
      "Content": "Content",
    }
    widgets = {
      "Content": forms.Textarea(attrs={"class": "form-control"}),
    }
