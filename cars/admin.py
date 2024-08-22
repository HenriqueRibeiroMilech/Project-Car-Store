from django.contrib import admin
from cars.models import Car, Brand
               
               #Sempre herda
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'models_year', 'value') #cria uma grade com esses itens
    search_fields = ('model', 'brand', ) #faz ser possivel pesquisar usando esse campo

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

admin.site.register(Car, CarAdmin) #Adciona essa tabela com essas regras no admin
admin.site.register(Brand, BrandAdmin)
