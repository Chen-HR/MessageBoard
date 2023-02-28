from django.shortcuts import render, redirect
from Article.models import Article, Message
from Account.models import User
from Article.forms import ArticleForm, MessageForm

from datetime import datetime

# Create your views here.

def Article_Create(request):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    "State": [],
    "ArticleForm_valid": "Unverified", 
  }
  context["State"].append(context["RequestMethod"]) 
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState_old"] = "True"
    context["LogingState"] = "True"
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    context["State"].append("Confirm_Login_True")
  else:
    context["LogingState"] = "False"
    context["State"].append("Confirm_Login_False")

  if context["RequestMethod"] == "POST":
    articleForm = ArticleForm(request.POST)
    if articleForm.is_valid():
      context["ArticleForm_valid"] = "Valid"
      context["State"].append("ArticleForm_Valid")
      # Get ArticleForm data
      GetArticleForm = False
      try: 
        articleTitle = articleForm.cleaned_data["Title"]
        articleContent = articleForm.cleaned_data["Content"]
        context["ArticleForm_Title"] = articleTitle
        context["ArticleForm_Content"] = articleContent
      except ValueError as Error:
        context["Error"] = "\n".join([context["Error"], Error])
        context["State"].append("Get_ArticleForm_Failed") 
        # GetArticleForm = False
      else:
        context["State"].append("Get_ArticleForm_Success") 
        GetArticleForm = True

      # Todo: data encoding ( for non-plaintext Query ( Prevent Insertion Attacks ) )

      # Add Article
      if GetArticleForm:
        articleAuthor = None
        if context["LogingState"] == "True":
          articleAuthorAccount = context["User_Account"]
          articleAuthorName = context["User_Name"]
          articleAuthor = User.objects.get(Account=context["User_Account"])
        else:
          articleAuthorAccount = ""
          articleAuthorName = "Anonymous"
          # pass
        context["Article_Author"] = articleAuthor
        try:
          article = Article.objects.create(Title=articleTitle, Content=articleContent, Author=articleAuthor) 
        except:
          context["Error"] = "\n".join([context["Error"], "Article.objects.create: Failed to apply for an article"])
          context["ErrorMessage_Submit"] = "Failed to apply for an article"
          context["State"].append("SaveArticle_Failed") 
        else:
          context["State"].append("SaveArticle_Success") 
          return redirect("/article/{}".format(article.id))

      
      # authorAccount = 
      # article = messageForm.save(commit=False)
      # author = User.objects.get(Account=request.session["Account"])
      # article.author = author
      # article.save()
      # messages.success(request, "Article created successfully.")
    else:
      context["State"].append("ArticleForm_InValid")
  else:
    articleForm = ArticleForm()
  context["ArticleForm"] = articleForm
  return render(request, "ArticleCreate.html", context)

def Article_List(request):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    "State": [],
    # "LogoutForm_valid": "Unverified", 
  }
  context["State"].append(context["RequestMethod"]) 
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState_old"] = "True"
    context["LogingState"] = "True"
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    context["State"].append("Confirm_Login_True")
  else:
    context["LogingState"] = "False"
    context["State"].append("Confirm_Login_False")

  # Get all Article
  try:
    ArticleList = Article.objects.all().order_by("ReleaseTime")
  except:
    context["Error"] = "\n".join([context["Error"], "Error: Article_List > Get_all_Article > `Article.objects.all().order_by(\"ReleaseTime\")`"])
    context["State"].append("GetArticle_Failed") 
  else:
    context["ArticleList"] = ArticleList
    context["State"].append("GetArticle_Success") 
  return render(request, "ArticleList.html", context)

def Article_Content(request, ArticleId):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    "State": [],
    "ArticleId": ArticleId, 
    "MessageForm_valid": "Unverified", 
  }
  context["State"].append(context["RequestMethod"]) 
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState_old"] = "True"
    context["LogingState"] = "True"
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    context["State"].append("Confirm_Login_True")
  else:
    context["LogingState"] = "False"
    context["State"].append("Confirm_Login_False")

  # Get Article with id
  try:
    article = Article.objects.get(pk=ArticleId)
  except:
    context["Error"] = "\n".join([context["Error"], "Error: Article_List > Get_Article_with_id > `Article.objects.get(pk=ArticleId)`"])
    context["State"].append("GetArticle_Failed") 
  else:
    context["Article"] = article
    context["State"].append("GetArticle_Success") 
  
  # Add new message
  if context["RequestMethod"] == "POST":
    messageForm = MessageForm(request.POST)
    if messageForm.is_valid():
      context["MessageForm_valid"] = "Valid"
      context["State"].append("MessageForm_Valid")
      # Get MessageForm data
      GetMessageForm = False
      try: 
        messageContent = messageForm.cleaned_data["Content"]
        context["MessageForm_Content"] = messageContent
      except ValueError as Error:
        context["Error"] = "\n".join([context["Error"], Error])
        context["State"].append("Get_MessageForm_Failed") 
        # GetMessageForm = False
      else:
        context["State"].append("Get_MessageForm_Success") 
        GetMessageForm = True

      # Todo: data encoding ( for non-plaintext Query ( Prevent Insertion Attacks ) )

      # Add Message
      if GetMessageForm:
        messageAuthor = None
        if context["LogingState"] == "True":
          messageAuthorAccount = context["User_Account"]
          messageAuthorName = context["User_Name"]
          messageAuthor = User.objects.get(Account=context["User_Account"])
        else:
          messageAuthorAccount = ""
          messageAuthorName = "Anonymous"
          # pass
        context["Message_Author"] = messageAuthor
        try:
          Message.objects.create(Article=article, Content=messageContent, Author=messageAuthor) 
        except:
          context["Error"] = "\n".join([context["Error"], "Message.objects.create: Failed to apply for an message"])
          context["ErrorMessage_Submit"] = "Failed to apply for an article"
          context["State"].append("AddMessage_Failed") 
        else:
          context["State"].append("AddMessage_Success") 
          return redirect("/article/{}".format(ArticleId))
    else:
      context["MessageForm_valid"] = "InValid"
      context["State"].append("MessageForm_InValid")
  else:
    messageForm = MessageForm()
  context["MessageForm"] = messageForm

  # Get all Message in this Article
  try:
    MessageList = Article.objects.get(pk=ArticleId).Message.all().order_by("ReleaseTime")
  except:
    context["Error"] = "\n".join([context["Error"], "Error: Article_Content > Get_all_Message_in_this_Article > `article.message.all().order_by(\"ReleaseTime\")`"])
    context["State"].append("GetMessageList_Failed") 
  else:
    context["MessageList"] = MessageList
    context["State"].append("GetMessageList_Success") 

  return render(request, "ArticleContent.html", context)
