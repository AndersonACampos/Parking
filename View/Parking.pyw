import sys
import os
import PySimpleGUI as sg
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb
import time
import Ticket

try:
    ticket, colunas = tb.buscar_todos();
except Exception as ex:
    sg.popup_error(ex)

sg.theme('TanBlue')

layout = [
    [sg.Table(ticket, 
              colunas, 
              justification="center",
              auto_size_columns=False,
              col_widths=[6,15,15,8,10,15], 
              font=("Arial", "10", "bold"),
              enable_events=True,
              key='grdTickets'
              )],
    
    [sg.Button("Fechar", 
               key='cmdFechar'
               )]
]

window = sg.Window("Park v1.0", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,"cmdFechar") :
        break
    if event == 'grdTickets':
        linha = values['grdTickets'][0]
        Ticket.fechar_conta(ticket[linha])        
window.close()