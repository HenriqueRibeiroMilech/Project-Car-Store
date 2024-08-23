from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self): #quando a aplicaçao cars for iniciada
        import cars.signals #ele vai importar o arquivo signals.py
