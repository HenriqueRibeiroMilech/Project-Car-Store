from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

### Cars View com Classe usando ListView ### 
class CarListView (ListView): #isso é uma view que vai listar coisas (por isso ele ja sabe que é get)

    model = Car #To dizendo que o model dessa views é Car
    template_name = 'cars.html' #que o template que ele vai usar é esse
    context_object_name ='cars' #e o nome do objeto uq vai passr pro template é esse

    def get_queryset(self):#função de pesquisa do ListView
        cars = super().get_queryset().order_by('model') #ele pega todos os carros do banco de dados e ordena
        search = self.request.GET.get('search') #Ele captura o que o usuario pesquisou 
        if search: #se ele tiver alguma pesquisa
            cars = cars.filter(model__icontains=search) #ele filtra pela pesquisa
        return cars


### New Cars View com Classe usando CreateView ###
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView): #isso é uma view que cria algo(carro) (por isso ele ja sabe que é CreateView) 
                                                                          #(Ja como é uma CreatView ele sabe que vai ter get e post )
    model = Car #To dizendo que o model dessa views é Car
    form_class = CarModelForm # to dizendo que o formulario que ele vai usar
    template_name = 'new_car.html' #que o template que ele vai usar é esse
    success_url = '/cars/' #to dizendo que quando ele castrar algo com sucesso vai enviar para ca


class CarDetailView(DetailView): # vai mostra um objeto detalhado (clica em um carro na lista de carros e ela mostra os detalhes daquele carro)
    model = Car #To dizendo que o model dessa views é Car
    template_name = 'car_detail.html' #que o template que ele vai usar é esse

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView): #vai ser uma view para atualizar os carros
    model = Car #To dizendo que o model dessa views é Car
    form_class = CarModelForm # to dizendo que o formulario que ele vai usar
    template_name = 'car_update.html' #que o template que ele vai usar é esse
    success_url = '/cars/' #to dizendo que quando ele castrar algo com sucesso vai enviar para car

    def get_sucess_url(self):
        return reverse_lazy('car_detail', kwargs ={'pk': self.object.pk}) # se der sucesso ele vai me mandar para essa pagina

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car #To dizendo que o model dessa views é Car
    template_name = 'car_delete.html' #que o template que ele vai usar é esse
    success_url = '/cars/' #to dizendo que quando ele castrar algo com sucesso vai enviar para car