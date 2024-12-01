import sys
import os
import PySimpleGUI as sg
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb
import Pagamento
import Ticket

sg.theme('TanBlue')

def carrega_ticket():
    try:
        ticket, colunas = tb.buscar_todos();
        return ticket, colunas
    except Exception as ex:    
        sg.popup_error(f'{ex} - {ex.args}')

ticket, colunas = carrega_ticket()

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
    
    [sg.Button("Fechar", key='cmdFechar'), sg.Button("Cadastrar", key='cmdCadastrar')]
]

window = sg.Window("Park v1.0", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED,"cmdFechar") :
        break
    
    if event == 'grdTickets':
        try:
            linha = values['grdTickets'][0]
            Pagamento.fechar_conta(ticket[linha])
        except:
            pass
        ticket, colunas = carrega_ticket()
        window['grdTickets'].update(values=ticket)
        
    if event == 'cmdCadastrar':
        Ticket.cadastrar()
             
window.close()