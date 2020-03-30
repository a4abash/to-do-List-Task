from django.shortcuts import redirect,render
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login,logout,authenticate
from features.forms import featureForm
from django.contrib.auth.models import User
from features.models import TaskFeatures
from django.contrib.auth.decorators import login_required


# home page
def home(request):
    return render(request, 'index.html')


# signup page
def signup(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm()
        }
        return render(request, 'signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your acccount is created successfully")
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form':form})


# login page
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("error occured")
            messages.error(request, "Your Password does not match")
            return redirect('signin')


# user dashboard
@login_required(login_url='signin')
def dashboard(request):
    if request.method == 'GET':
        a = User.objects.get(id=request.user.id)
        details = TaskFeatures.objects.filter(user_id=a)
        context = {
            'form': featureForm(),
            'details': details
        }
        return render(request, 'dashboard.html', context)
    else:
        form = featureForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'dashboard.html', {'form': form})


# code to delete the task
def taskdelete(request, x):
    s = TaskFeatures.objects.filter(id=x)
    s.delete()
    return redirect('dashboard')


# for signout
def signout(request):
    logout(request)
    return redirect('signin')