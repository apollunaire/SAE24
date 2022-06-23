from django.urls import path
from . import views

urlpatterns = [
    path('affichecapteur/', views.affichecapteur),
    path('updatecapteur/', views.updatecapteur),
    path('traitementupdatecapteur/<int:id>', views.traitementupdatecapteur),
    ]