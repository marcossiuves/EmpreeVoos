# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:00:41 2021

@author: marcos
"""

from django.urls import path
from .views import get_index, detalhar_agendamento, retirar_agendamento, criar_agendamento


urlpatterns = [    
    path('', get_index, name='index'),
    path('agendamentos', detalhar_agendamento, name='detalhes_agendamentos'),
    path('novoAgendamento/', criar_agendamento, name='criar_agendamento'),
    path('remover/<int:id_agendamento>/', retirar_agendamento, name='retirar_agendamento'),

] 
