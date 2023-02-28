from django.db import models
from Account.models import User

# Create your models here.
class Article(models.Model):
  Title       = models.CharField(max_length=128)
  Author      = models.ForeignKey(User, on_delete=models.SET("Deleted User"), related_name="Article", default="Anonymous", null=True)
  ReleaseTime = models.DateTimeField(auto_now_add=True)
  Content     = models.TextField()
  def __str__(self):
    return self.Title

class Message(models.Model):
  Article     = models.ForeignKey(Article, on_delete=models.SET("Deleted Article"), related_name="Message", default="None")
  Author      = models.ForeignKey(User, on_delete=models.SET("Deleted User"), related_name="Message", default="Anonymous", null=True)
  ReleaseTime = models.DateTimeField(auto_now_add=True)
  Content     = models.TextField()
  def __str__(self):
    return self.Content[:32]
