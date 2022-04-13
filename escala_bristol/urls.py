from django.urls import path

from . import views

urlpatterns = [
    path('history', views.history),
    # path('', views.index, name='index'),
    path('', views.scale),
    path('interpretation', views.interpretation),
    path('scale', views.scale),
    path('uses', views.uses),
]