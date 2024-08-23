from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_inventory_update(): #Funçao que recalcula o estoque e salva no banco de dados

    cars_count = Car.objects.all().count() #recebe a quantidade de carros que temos no banco de dados
    cars_value = Car.objects.aggregate( 
        total_value=Sum('value')        #vai retornar a soma dos valores dos nossos carros
    )['total_value']
    CarInventory.objects.create( #crai um registro novo no banco de dados
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car) #é uma função que deve ser executada no pos save de Car
def car_pos_save(sender, instance, **kwargs): # e manda ela para executar isso
    car_inventory_update()

@receiver(post_delete, sender=Car) #é uma função que deve ser executada no pos Delete de Car
def car_pos_delete(sender, instance, **kwargs): # e manda ela para executar isso
    car_inventory_update()
