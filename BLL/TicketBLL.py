import math
import sys
import os
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAL.TicketDAL as td
from datetime import datetime
import math


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

    # Definir os horários como objetos datetime
    hora_inicial = datetime.strptime(entrada, "%d/%m/%Y %H:%M:%S")
    hora_final = datetime.strptime(saida, "%d/%m/%Y %H:%M:%S")

    # Calcular a diferença entre os horários
    diferenca = hora_final - hora_inicial

    # Converter a diferença para minutos
    diferenca_em_minutos = diferenca.total_seconds() / 60

    return math.ceil(diferenca_em_minutos)


def calcular_valor_pagar(entrada_em_minutos):
    # Regra 1: Se o tempo for até 30 minutos, o valor é R$ 10
    if entrada_em_minutos <= 30:
        return 10
    
    # Regra 2: Se o tempo for até 1 hora (60 minutos), o valor é R$ 20
    elif entrada_em_minutos <= 60:
        return 30
    
    minutos_restantes = entrada_em_minutos - 60

    # Regra 3: Para horas além de 1 hora, calcula R$ 10 por hora (arredondando para cima)
    valor_total = 30
    if minutos_restantes > 0:
        horas = math.ceil(minutos_restantes / 60)
        valor_total += horas * 10  # R$ 10 por hora, arredondando para cima

    return valor_total



