
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView, CarListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarListView.as_view(), name='cars_list'), #precisa colocar o (Classe.as_view()) para funcionar unsando uma view em classe
    path('register/', register_view, name='register'), 
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'),  
    path('new_car/', NewCarCreateView.as_view(), name='new_car'), #precisa colocar o (Classe.as_view()) para funcionar unsando uma view em classe  
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'), #Detalhamento do carro - pk = premordy keay
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'), #Atualizar carro - pk = premordy keay
    path('car/<int:pk>/delet/', CarDeleteView.as_view(), name='car_delete') #Atualizar carro - pk = premordy keay
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
