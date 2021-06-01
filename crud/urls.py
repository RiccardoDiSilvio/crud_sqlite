from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.MainMenuView),
    path('animal/', views.AnimalCrudView.as_view()),
    path('alimentacion/', views.AlimentacionCrudView.as_view()),
    path('cita_control/', views.CitaDeControlCrudView.as_view()),
    path('inseminacion/', views.InseminacionCrudView.as_view()),
    path('pajilla/', views.PajillaCrudView.as_view()),
    path('proceso/', views.ProcesoVeterinarioCrudView.as_view()),
    path('venta/', views.VentaCrudView.as_view()),
    path('veterinario/', views.VeterinarioCrudView.as_view()),
    path('cambio_rol/', views.CambioDeRolList.as_view()),
]