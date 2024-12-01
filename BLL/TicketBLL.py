import math
import sys
import os
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAL.TicketDAL as td
from datetime import datetime
import math


def cadastrar(placa, carro, cor):
    if placa == '':
        raise NameError('A placa é obrigatória')
    if carro == '':
        raise NameError('A carro é obrigatório')
    if cor == '':
        raise NameError('A cor é obrigatória')
    
    td.cadastrar(placa, carro, cor)
        

def buscar_todos():
    ticket, colunas = td.buscar_todos();
    if len(ticket) == 0:
        raise NameError('Nenhum registro encontrado')
    return ticket, colunas


def pagar(id, saida, tempo, valor):

    ret = td.pagar(id, saida, tempo, valor)
    if ret:
        return True
    else:
        raise NameError("Ocorreu um erro ao pagar")
    

def calcula_tempo(entrada, saida):
    hora_inicial = datetime.strptime(entrada, "%d/%m/%Y %H:%M:%S")
    hora_final = datetime.strptime(saida, "%d/%m/%Y %H:%M:%S")
    diferenca = hora_final - hora_inicial
    diferenca_em_minutos = diferenca.total_seconds() / 60
    return math.ceil(diferenca_em_minutos)


def calcular_valor_pagar(entrada_em_minutos):
    if entrada_em_minutos <= 30:
        return 10
    elif entrada_em_minutos <= 60:
        return 30
    minutos_restantes = entrada_em_minutos - 60
    valor_total = 30
    if minutos_restantes > 0:
        horas = math.ceil(minutos_restantes / 60)
        valor_total += horas * 10
    return valor_total



