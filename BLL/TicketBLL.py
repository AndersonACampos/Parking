import sys
import os
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAL.TicketDAL as td

def buscar_todos():
    ticket, colunas = td.buscar_todos();
    if len(ticket) == 0:
        raise NameError('Nenhum registro encontrado')
    return ticket, colunas