from django.contrib import admin
from Account.models import User
from Article.models import Article, Message

# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Message)