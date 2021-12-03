from django.shortcuts import render, get_object_or_404
from .models import Destinos
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Agendamento
from .forms import AgendamentosForm

# Create your views here.

#from django.shortcuts import render


def get_index(request, slug_destinos=None):
    destino = None
    lista_destinos = Destinos.objects.all()

    if slug_destinos:
        destino = get_object_or_404(destino, slug=slug_destinos)
    contexto = {
        'destino': destino,
        'lista_destinos': lista_destinos,
    }
    return render(request, 'index.html', contexto)

def criar_agendamento(request):
    
    agendamentos = Agendamento(request)
    form =  AgendamentosForm(request.POST)
   
    destino = None
    lista_destinos = Destinos.objects.all()
   
    contexto = {
        'destino': destino,
        'lista_destinos': lista_destinos,
    }
    if form.is_valid():
        dados = form.cleaned_data
        agendamentos.adicionar(
            quantidade=dados['quantidade'],
            atualizar_quantidade=dados['atualizar'])
    return render(request, 'novoAgendamento.html', contexto)


def retirar_agendamento(request, id_agendamento):
    agendamento = Agendamento(request)
    agendamentos = get_object_or_404(Agendamento, id=id_agendamento)
    agendamentos.remover(agendamento)
    return redirect('detalhar_agendamento')


def detalhar_agendamento(request):
    agendamento = Agendamento(request)
    for item in agendamento:
        item['formulario_novo_agendamento'] = \
            AgendamentosForm(
                initial={'quantidade': item['quantidade'], 'atualizar': True})
    return render(request, 'agendamentos.html', {'agendamento': agendamento})

