from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')


def verityuser(request):
  e = request.POST["email"]
  # print(e)
  p = request.POST["password"]
  # print(p)
  try:
    User.objects.get(username=e).check_password(p)
  except:
    messages.success(request, "Details Not Match Please register")
    return redirect("login")
  else:
    return redirect("home")