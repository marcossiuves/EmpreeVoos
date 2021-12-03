from django.shortcuts import  render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, logout 
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():            
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastrado com sucesso!" )
            return render(request, 'index.html')
    messages.error(request, "Ooops... ocorreu algum erro no seu cadastro!")
    form = NewUserForm()
    return render (request=request, template_name="criar.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Agora você não está mais logado como {username}.")
                return render(request, 'index.html')
            else:
                messages.error(request,"Username ou senha incorretos")
        else:
            messages.error(request,"Username ou senha incorretos")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Até mais!!") 
    return render(request, 'logout.html')

def go_home(request):
    return render(request, 'index.html')

