# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:08:31 2021

@author: marcos
"""
from decimal import Decimal
from django.conf import settings
from main.models import Agendamento

class NovoAgendamento:

    def __init__(self, request):
        self.__sessao = request.session
        novoAgendamento = self.__sessao.get(settings.ID_AGENDAMENTO)
        if not novoAgendamento:
            novoAgendamento = self.__sessao[settings.ID_AGENDAMENTO] = {}
        self.__novoAgendamento = novoAgendamento

    def adicionar(self, destino, quantidadePessoas=1, atualizar_quantidade=False):
        id_agendamento = str(destino.id)
        if id_agendamento not in self.__novoAgendamento:
            self.__novoAgendamento[id_agendamento] = {
                'quantidade': 0,
                'preco': str(destino.precoPorPessoa),
            }
        if atualizar_quantidade:
            self.__novoAgendamento[id_agendamento]['quantidade'] = quantidadePessoas
        else:
            self.__novoAgendamento[id_agendamento]['quantidade'] += quantidadePessoas
        self.__salvar()

    def __salvar(self):
        self.__sessao[settings.ID_AGENDAMENTO] = self.__novoAgendamento
        self.__sessao.modified = True

    def remover(self, agendamento):
        id_agendamento = str(agendamento.id)
        if id_agendamento in self.__novoAgendamento:
            del self.__novoAgendamento[id_agendamento]
            self.__salvar()

    def __iter__(self):
        ids_agendamentos = self.__novoAgendamento.keys()
        agendamentos = Agendamento.objects.filter(id__in=ids_agendamentos)
        agendamento = self.__novoAgendamento.copy()
        for agendamento in agendamentos:
            agendamento[str(agendamento.id)]['destino'] = agendamento
        for item in agendamentos.values():
            item['precoPorPessoa'] = Decimal(item['precoPorPessoa'])
            item['subtotal'] = Decimal(item['precoPorPessoa']) * Decimal(item['quantidade'])
        yield item

    def __len__(self):
        resultado = 0
        for item in self.__agendamentos.values():
            resultado += item['quantidade']
        return resultado

    def get_total_geral(self):
        resultado = Decimal(0.0)
        for item in self.__agendamento.values():
            subtotal = Decimal(item['quantidade']) * Decimal(item['preco'])
            resultado = resultado + subtotal
        return resultado
