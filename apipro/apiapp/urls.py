from django.contrib import admin
from django.urls import path
from .import views

app_name = 'apiapp'

urlpatterns = [

    path('emp', views.emp,name='create'),
    path('show',views.show,name='retrieve'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy,name='destroy'),
]