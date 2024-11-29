import sys
import os
import PySimpleGUI as sg

sg.theme('Default1')

# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAL.TicketDAL as td


ticket, colunas = td.buscar_todos();

# print(ticket)

layout = [
    [sg.Table(ticket, colunas, justification="center",auto_size_columns=False,col_widths=[6,15,15,8,10,15], font=("Arial", "10", "bold"))],
    [sg.Button("Fechar", key='cmdFechar', )]
]

window = sg.Window("Park 1.0", layout)

while True:
    event, values = window.read()
    # print(event, values)
    if event in (sg.WINDOW_CLOSED,"cmdFechar") :
        break
    
window.close()