from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm): #necessario herdar isso para criar um formulario 

    class Meta:#cria a classe necessaria
        model = Car #form criado em cima do model Car
        fields = '__all__'  #campos que quer no formulario

    #Validação
    def clean_value(self): #clean_nome - sintaxe para validaçao no django
        value = self.cleaned_data.get('value') #capitura o conteudo do campo value na hora que o usuario tenta cadastrar
        if value < 20000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year <1975:
            self.add_error('factory_year', 'Nao aceitamos velharias!')
        return factory_year