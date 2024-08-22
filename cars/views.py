from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request): #Uma função que recebe uma requisiçao
    cars = Car.objects.all().order_by('model') #Ele busca todos os carros do banco de dados, os ordenando
    search = request.GET.get('search') #Ele captura o que o usuario pesquisa na url

    if search: #se ele tiver alguma pesquisa
        cars = Car.objects.filter(model__icontains=search) #ele filtra pela pesquisa

    return render(request, 'cars.html', {'cars': cars} ) #ele renderiza uma template e manda para o arquivo html esse modelo

def new_car_view(request):
    if request.method == 'POST':    #Verifica se o http ta mandando um post(enviando algo para o sistema)
        new_car_form = CarModelForm(request.POST, request.FILES)    #adiciona o Conteudo e Arquivos do formulario nessa variavel
        if new_car_form.is_valid(): #se o formulario for valido(atende todos os requisitos da validação)
            new_car_form.save() #ele envia para o banco de dados
            return redirect('cars_list') # e redireciona o usuario para a pagina dos carros
    else:   #Se o http for um Get(ou seja estiver somente querendo exibir a pagina)
        new_car_form = CarModelForm()   #ele salva um formulario vazio nessa variavel
    return render(request, 'new_car.html', { 'new_car_form': new_car_form })    #depois ele renderiza o nosso template