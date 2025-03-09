from django.contrib import admin
from django.urls import path
from .views import Home, OperationsList


urlpatterns = [
    path('', Home.as_view(), name='operations-home'),
    path('operations', OperationsList.as_view(), name='operations-list'),

]