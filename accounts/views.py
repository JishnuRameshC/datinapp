from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginFrom,UserCreationForm

# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = LoginFrom()
        return render(request, 'accounts/login.html', context)
    elif request.method == 'POST':
        form = LoginFrom(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(f'User login successfull  (username  :  {username})')
            else:
                return HttpResponse('Login failed')
        
        # If the form is not valid.
        context['form'] = form
        return render(request, 'accounts/login.html', context)

def register(request):
    context = {}
    if request.method == 'GET':
        context['form']  = UserCreationForm()
        return render(request,'accounts/register.html',context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if not form.is_valid():
            context['form'] = form
            return render(request, 'accounts/registation.html', context)

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return HttpResponse(f'User registration successfull')
    

def demo(request):
    context = {}
    if request.method == 'GET':
        context['form']  = UserCreationForm()
        return render(request,'accounts/demo.html',context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if not form.is_valid():
            context['form'] = form
            return render(request, 'accounts/demo.html', context)

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return HttpResponse(f'User registration successfull')
        

