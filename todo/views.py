from django.shortcuts import redirect,render
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login,logout,authenticate


def home(request):
    return render(request, 'index.html')


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


def dashboard(request):
    return render(request,'dashboard.html')


# for signout
def signout(request):
    logout(request)
    return redirect('signin')