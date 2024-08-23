from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

          #sempre vai herdar esse models para criar as tabelas
class Car(models.Model):    #cria uma "tabela"
                #(AutoField) ele vai se incrementando (1,2,3...)
    id = models.AutoField(primary_key=True) #ele é uma chave primaria
                   #(CharField) vai ser um campo de String
    model = models.CharField(max_length=200) #tamanho maximo
                   #(ForeignKey) agora o atributo brand ele vai estar ligado a uma tabela brand
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #(on_delete=models.PROTECT) não pode deletar a brand
                   #Inteiros
    factory_year = models.IntegerField(blank=True, null=True) #Pode ficar vazio esse campo
    models_year = models.IntegerField(blank=True, null=True)

    plate = models.CharField(max_length=10, blank=True, null=True)
                   #FLoat
    value = models.FloatField(blank=True, null=True)
                    #Usar uma imagem
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
                                        #salva na pasta (cars)
    bio = models.TextField(blank=True, null=True) #é um texto

    def __str__(self):  #Deixa os nomes mais bonitos e muda algo na aplicação (FAZER)
        return self.model

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) #automaticamente daciona a data e hora automatico

    class Meta:
        ordering = ['-created_at'] #ordena da data mais nova 

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'