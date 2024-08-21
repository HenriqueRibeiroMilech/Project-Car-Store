from django.contrib.auth.forms import UserCreationForm, AuthenticationForm   #Importação necessaria para fazer esse sistema
from django.shortcuts import render, redirect                     #Para criar Usuarios (UserCreationForm) e para logar (AuthenticationForm)
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST': #Verifica se o http ta mandando um post(enviando algo para o sistema)
        user_form = UserCreationForm(request.POST) #adiciona o Conteudo do formulario de criaçao de conta nessa variavel

        if user_form.is_valid():  #se o formulario for valido(atende todos os requisitos da validação)
            user_form.save() #ele envia para o banco de dados
            return redirect('login') #e redireciona o usuario para a pagina login
        
    else:   #Se o http for um Get(ou seja estiver somente querendo exibir a pagina)
        user_form = UserCreationForm() #Ele cria um Formulario pronto do django para criar ususarios vazio

    return render(request, 'register.html', {'user_form': user_form}) #depois ele renderiza o nosso template



def login_view(request):
    if request.method == 'POST': #Verifica se o http ta mandando um post(enviando algo para o sistema)
        username = request.POST["username"] #Salva o username que o usuario digito em uma variavel
        password = request.POST["password"] #mesma cois mas em password
        user = authenticate(request, username=username, password=password) #verifica se o usuario e senha está correto e salva na variavel (import authenticate)

        if user is not None: # se o usuario não for nulo
            login(request, user) #faz o login
            return redirect('cars_list')

        else: # se não
            login_form = AuthenticationForm() #retorna um formulario vazio (import login)

    else:   #Se o http for um Get(ou seja estiver somente querendo exibir a pagina)
        login_form = AuthenticationForm() #retorna um formulario vazio

    return render (request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request) #faz o logout da conta (import logout)
    return redirect('cars_list') #retorna para a tela de carros