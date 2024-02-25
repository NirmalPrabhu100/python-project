from django.urls import path
from app import views
urlpatterns = [
    path('one/', views.onefun,name='onefun'),
    path('sucess/', views.twofun,name='twofun'),

]