from django.shortcuts import render, redirect
from Account.models import User
from Account.forms import SignupForm, LoginForm
from django.core import exceptions as DjangoExceptions

from datetime import datetime

# Create your views here.
def Account_Signup(request):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    # "State": "",
    "State": [],
    "SignupForm_valid": "Unverified", 
  }
  # context["State"] = context["RequestMethod"]
  context["State"].append(context["RequestMethod"]) 
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState"] = "True"
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    # context["State"] = " > ".join([context["State"], "Confirm_Login_Successful"])
    context["State"].append("Confirm_Login_True") 
  else:
    context["LogingState"] = "False"
    # context["State"] = " > ".join([context["State"], "Confirm_Login_Failed"])
    context["State"].append("Confirm_Login_False") 

  if context["RequestMethod"] == "POST":
    signupForm = SignupForm(request.POST)
    if signupForm.is_valid():
      context["SignupForm_valid"] = "Valid"
      # context["State"] = " > ".join([context["State"], "SignupForm_Valid"])
      context["State"].append("SignupForm_Valid") 
      # Get SignupForm data
      GetInformation = False
      try: 
        SignupForm_Account    = signupForm.cleaned_data["Account"]
        SignupForm_Password   = signupForm.cleaned_data["Password"]
        SignupForm_RePassword = signupForm.cleaned_data["RePassword"]
        SignupForm_Name       = signupForm.cleaned_data["Name"]
        SignupForm_Phone      = signupForm.cleaned_data["Phone"]
        SignupForm_Email      = signupForm.cleaned_data["Email"]
        context["SignupForm_Account"]    = SignupForm_Account    
        context["SignupForm_Password"]   = SignupForm_Password   
        context["SignupForm_RePassword"] = SignupForm_RePassword 
        context["SignupForm_Name"]       = SignupForm_Name       
        context["SignupForm_Phone"]      = SignupForm_Phone      
        context["SignupForm_Email"]      = SignupForm_Email      
      except ValueError as Error:
        context["Error"] = "\n".join([context["Error"], Error])
        # context["State"] = " > ".join([context["State"], "SignupForm_Get_Failed"])
        context["State"].append("SignupForm_Get_Failed") 
        # GetInformation = False
      else:
        # context["State"] = " > ".join([context["State"], "SignupForm_Get_Success"])
        context["State"].append("SignupForm_Get_Success") 
        GetInformation = True

      # Todo: data encoding ( for non-plaintext Query ( Prevent Insertion Attacks ) )

      # Password Confirmation
      ConfirmationPassword = False
      if SignupForm_Password != SignupForm_RePassword:
        context["ErrorMessage_Password"] = "The two passwords entered are different"
        # context["ErrorMessage"] = "\n".join([context["ErrorMessage"], context["ErrorMessage_Password"]])
        # context["State"] = " > ".join([context["State"], "Confirmation_Password_Failed"])
        context["State"].append("Confirmation_Password_Failed") 
        ConfirmationPassword = False
      else:
        # context["State"] = " > ".join([context["State"], "Confirmation_Password_Success"])
        context["State"].append("Confirmation_Password_Success") 
        ConfirmationPassword = True
      
      # Confirm there are no duplicate accounts
      VerifyUniqueness = False
      try:
        AccountQuerying = User.objects.get(Account=context["SignupForm_Account"])
      except DjangoExceptions.MultipleObjectsReturned as Error: # Multiple accounts with the same name
        context["Error"] = "\n".join([context["Error"], "The query returned multiple objects when only one was expected."])
        # context["ErrorMessage_Account"] = "This account name is already in use"
        # context["ErrorMessage"] = "\n".join([context["ErrorMessage"], context["ErrorMessage_Account"]])
        # context["State"] = " > ".join([context["State"], "Duplicate Account"])
        # VerifyUniqueness = False
      except DjangoExceptions.ObjectDoesNotExist as Error: # Account name not yet used
        context["Error"] = "\n".join([context["Error"], "The requested object does not exist."])
        # context["State"] = " > ".join([context["State"], "Account Not Exist"])
        VerifyUniqueness = True
      # else: # have an account with the same name
      #   # context["ErrorMessage_Account"] = "This account name is already in use"
      #   # context["ErrorMessage"] = "\n".join([context["ErrorMessage"], context["ErrorMessage_Account"]])
      #   # context["State"] = " > ".join([context["State"], "Duplicate Account"])
      #   # VerifyUniqueness = False
      #   pass
      if VerifyUniqueness: # new account
        # context["State"] = " > ".join([context["State"], "Verify_Uniqueness_Success"])
        context["State"].append("Verify_Uniqueness_Success") 
      else: # Duplicate Account
        context["ErrorMessage_Account"] = "This account name is already in use"
        # context["ErrorMessage"] = "\n".join([context["ErrorMessage"], context["ErrorMessage_Account"]])
        # context["State"] = " > ".join([context["State"], "Verify_Uniqueness_Failed"])
        context["State"].append("Verify_Uniqueness_Failed") 

      # Save SignupForm to User
      if GetInformation and ConfirmationPassword and VerifyUniqueness:
        try:
          User.objects.create(Account=context["SignupForm_Account"], Password=context["SignupForm_Password"], Name=context["SignupForm_Name"], Phone=context["SignupForm_Phone"], Email=context["SignupForm_Email"]) 
        except:
          context["Error"] = "\n".join([context["Error"], "User.objects.create: Failed to apply for an account"])
          context["ErrorMessage_Submit"] = "Failed to apply for an account"
          # context["ErrorMessage"] = "\n".join([context["ErrorMessage"], context["ErrorMessage_Submit"]])
          # context["State"] = " > ".join([context["State"], "Save_Failed"])
          context["State"].append("Save_Failed") 
        else:
          # context["State"] = " > ".join([context["State"], "Save_Success"])
          context["State"].append("Save_Success") 
          return redirect("/account/login")
      
    else:
      context["SignupForm_valid"] = "Invalid"
      # context["State"] = " > ".join([context["State"], "SignupForm_Invalid"])
      context["State"].append("SignupForm_Invalid") 
  else:
    signupForm = SignupForm()
  context["SignupForm"] = signupForm
  return render(request, "AccountSignup.html", context)

def Account_Login(request):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    # "State": "",
    "State": [],
    "LoginForm_valid": "Unverified", 
  }
  # context["State"] = context["RequestMethod"]
  context["State"].append(context["RequestMethod"]) 
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState_old"] = "True"
    context["LogingState"] = "True"
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    # context["State"] = " > ".join([context["State"], "login"])
    context["State"].append("Confirm_Login_True")
  else:
    # context["LogingState_old"] = "False"
    context["LogingState"] = "False"
    # context["State"] = " > ".join([context["State"], "not_logged_in"])
    context["State"].append("Confirm_Login_False")
  
  if context["RequestMethod"] == "POST":
    loginForm = LoginForm(request.POST)
    if loginForm.is_valid():
      context["LoginForm_valid"] = "Valid"
      # context["State"] = " > ".join([context["State"], "Valid"])
      context["State"].append("LoginForm_Valid")
      # Get LoginForm data
      GetInformation = False
      try: 
        Account    = loginForm.cleaned_data["Account"]
        Password   = loginForm.cleaned_data["Password"]
        context["LoginForm_Account"]    = Account 
        context["LoginForm_Password"]   = Password
      except ValueError as Error:
        context["Error"] = "\n".join([context["Error"], Error])
        # context["State"] = " > ".join([context["State"], "read failed"])
        context["State"].append("LoginForm_Get_Failed")
        # GetInformation = False
      else:
        context["State"].append("LoginForm_Get_Success")
        GetInformation = True

      # Todo: data encoding ( for non-plaintext Query ( Prevent Insertion Attacks ) )

      # Confirm there are no duplicate accounts
      if GetInformation:
        AccountConfirmation = False
        try: # Query Account
          AccountQuerying = User.objects.get(Account=context["LoginForm_Account"], Password=context["LoginForm_Password"])
        except DjangoExceptions.MultipleObjectsReturned as Error: # Multiple accounts with the same name
          context["Error"] = "\n".join([context["Error"], "The query returned multiple objects when only one was expected."])
          # context["State"] = " > ".join([context["State"], "Duplicate_Account"])
          context["State"].append("Account_Existence_Multiple")
          # AccountConfirmation = False
        except DjangoExceptions.ObjectDoesNotExist as Error: # Account name not yet used
          # context["Error"] = "\n".join([context["Error"], "The requested object does not exist."])
          # context["State"] = " > ".join([context["State"], "Account_Not_Exist"])
          context["State"].append("Account_Existence_NotExist")
          # AccountConfirmation = False
        else: # have an account with the same name
          # context["State"] = " > ".join([context["State"], "login_successfully"])
          context["State"].append("Account_Existence_Unique")
          AccountConfirmation = True
        if AccountConfirmation: # login successfully
          context["LogingState"] = "True"
          context["User_Account"] = AccountQuerying.Account
          context["User_Name"] = AccountQuerying.Name
          request.session["Account"] = AccountQuerying.Account
          request.session["Name"] = AccountQuerying.Name
          context["State"].append("Confirm_Login_True")
          # return redirect("/")
        else: # login fail
          context["ErrorMessage_Submit"] = "Account or password is incorrect or does not exist."
          # context["ErrorMessage"] = "\n".join([context["ErrorMessage"], context["ErrorMessage_Submit"]])
          # context["State"] = " > ".join([context["State"], "Duplicate Account"])
    else:
      context["LoginForm_valid"] = "Invalid"
      # context["State"] = " > ".join([context["State"], "Invalid"])
      context["State"].append("LoginForm_InValid")
  else:
    loginForm = LoginForm()
  context["LoginForm"] = loginForm
  return render(request, "AccountLogin.html", context)

def Account_Logout(request):
  # Create initial information
  context = {
    "DateTime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
    "RequestMethod": request.method, 
    "Error": "", 
    # "State": "",
    "State": [],
    # "LogoutForm_valid": "Unverified", 
  }
  # context["State"] = context["RequestMethod"]
  context["State"].append(context["RequestMethod"]) 
  # Get login status
  if "Account" in request.session and "Name" in request.session:
    context["LogingState_old"] = "True"
    context["LogingState"] = "True"
    context["User_Account_old"] = request.session["Account"]
    context["User_Account"] = request.session["Account"]
    context["User_Name"] = request.session["Name"]
    # context["State"] = " > ".join([context["State"], "login"])
    context["State"].append("Confirm_Login_True")
  else:
    # context["LogingState_old"] = "False"
    context["LogingState"] = "False"
    # context["State"] = " > ".join([context["State"], "not_logged_in"])
    context["State"].append("Confirm_Login_False")
  # Remove login infomation
  if context["LogingState"] == "True" and context["RequestMethod"] == "POST":
    context["LogingState"] = "False"
    context["User_Account"] = ""
    context["User_Name"] = ""
    del request.session["Account"]
    del request.session["Name"]
    context["State"].append("Confirm_Login_False")
    # return redirect("/account/login")
  return render(request, "AccountLogout.html", context)