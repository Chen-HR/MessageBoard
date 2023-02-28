"""MessageBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Account import views as Account
from Article import views as Article

from django.shortcuts import render, redirect
from datetime import datetime


def Guide(request):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    "State": "",
  }
  context["State"] = context["RequestMethod"]
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState"] = "True"
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    context["State"] = " > ".join([context["State"], "Confirm_Login_Successful"])
  else:
    context["LogingState"] = "False"
    context["State"] = " > ".join([context["State"], "Confirm_Login_Failed"])
  return render(request, "LinkPage.html", context)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", Article.Article_List, name="Home"),
    path("guide", Guide, name="Guide"),

    path("account/signup", Account.Account_Signup, name="AccountSignup"),
    path("account/login" , Account.Account_Login , name="AccountLogin" ),
    path("account/logout", Account.Account_Logout, name="AccountLogout"),
    
    path("article/create" , Article.Article_Create , name="ArticleCreate" ),
    # path("article/list"   , Article.Article_List   , name="ArticleList"   ),
    # path("article/content/<int:ArticleId>", Article.Article_Content, name="ArticleContent"),
    path("article/<int:ArticleId>", Article.Article_Content, name="Article"),

    # path("article/list", Article.article_list, name="article_list"),
    # path("article/create", Article.article_create, name="article_create"),
    # path("article/<int:pk>", Article.article_detail, name="article_detail"),
]
