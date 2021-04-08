from django.urls import path
from . import views

urlpatterns = [
    path('padre/', views.PadreCrudView),
    path('hijo/', views.HijoCrudView),
]