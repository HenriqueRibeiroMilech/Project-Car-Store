from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)

    return render(request, 'cars.html', {'cars': cars} )

def new_car_view(request):
    if request.method == 'POST':    #Verifica se o http ta mandando um post(enviando algo para o sistema)
        new_car_form = CarModelForm(request.POST, request.FILES)    #adiciona o Conteudo e Arquivos do formulario nessa variavel
        if new_car_form.is_valid(): #se o formulario for valido(atende todos os requisitos da validação)
            new_car_form.save() #ele envia para o banco de dados
            return redirect('cars_list') # e redireciona o usuario para a pagina dos carros
    else:   #Se o http for um Get(ou seja estiver somente querendo exibir a pagina)
        new_car_form = CarModelForm()   #ele salva um formulario vazio nessa variavel
    return render(request, 'new_car.html', { 'new_car_form': new_car_form })    #depois ele renderiza o nosso template