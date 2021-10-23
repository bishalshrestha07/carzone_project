from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    passcode = request.POST['Password']

    user = auth.authenticate(username=username, password=passcode)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('dashboard')

    else:
      messages.error(request,' Invalid login credential')
      return redirect('login')
  return render(request,'accounts/login.html')

def register(request):
  if request.method == 'POST':
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already exits!')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request,'Email already exitst!')
          return redirect(register)
        else:
          user = User.objects.create_user(first_name= firstname, last_name= lastname,username=username, password= password, email= email)
          auth.login(request, user)
          messages.success(request, ' You are now logged in!')
          return redirect('dashboard')
          user.save()
          messages.success(request,'You are registered successfully')
          return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')
  else:
    return render(request,'accounts/register.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    
    return redirect('home')
  return redirect('home')

@login_required(login_url= 'login')
def dashboard(request):
  user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
  data = {
    'inquiries':user_inquiry,
  }
  return render(request,'accounts/dashboard.html',data)