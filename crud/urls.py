from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.MainMenuView),
    path('padre/', views.PadreCrudView),
    path('hijo/', views.HijoCrudView),
    path('consulta1/', views.Consulta1View),
    path('consulta2/', views.Consulta2View),
    path('consulta3/', views.Consulta3View),
    path('consulta4/', views.Consulta4View),
]