from django.urls import path
from . import views

urlpatterns = [
    path('enter/', views.enter_patient_data, name='enter_patient_data'),
    path('summary/', views.patient_summary, name='patient_summary'),
    path('clear_data/', views.clear_patient_data, name='clear_patient_data'), 
]
