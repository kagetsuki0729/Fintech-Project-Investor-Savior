from django.urls import path

from . import views

app_name='savior'

urlpatterns = [
    path('', views.index, name='home'),
    path('diagram',views.diagram, name='diagram'),
    path('gtrend',views.gtrend, name='gtrend')
]