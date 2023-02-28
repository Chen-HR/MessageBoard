from django.db import models

# Create your models here.
class User(models.Model):
  # _id       = models.IntegerField(_("id"), primary_key=True)
  Account  = models.CharField(max_length=32, null=False)
  Password = models.CharField(max_length=32, null=False)
  Name     = models.CharField(max_length=64, null=False)
  Phone    = models.CharField(max_length=64, blank=True, default='')
  Email    = models.EmailField(max_length=256, blank=True, default='')
  Jointime = models.DateTimeField(auto_now=False, auto_now_add=True)
  def __str__(self):
    return self.Name+"("+self.Account+")"