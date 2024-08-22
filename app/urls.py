
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
        #direcionamento da url
    path('cars/', cars_view, name='cars_list'), #apelido para usar no sistema django
    path('register/', register_view, name='register'), #Url da pagina para se registrar
    path('login/', login_view, name='login'),   #Url da pagina para logar
    path('logout/', logout_view, name='logout'),   #Url da pagina para deslogar
    path('new_car/', new_car_view, name='new_car'),   #Url da pagina para criar novos carros
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
