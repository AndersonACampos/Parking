import os
import sys
import PySimpleGUI as sg
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb

def fechar_conta(ticket):
    
    codigo = str(ticket[0]).zfill(6)
    entrada = datetime.strptime( ticket[1],'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
    saida = datetime.strptime( ticket[2],'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S') if ticket[2] != '' else datetime.now().strftime('%d/%m/%Y %H:%M:%S') 
    tempo = tb.calcula_tempo(entrada, saida)
    pagar = f"R$ {tb.calcular_valor_pagar(tempo):,.2f}"
    
    coluna_esqueda = [
        [sg.Text(f'Ticket:')],
        [sg.Text(f'Hora da Entrada:')],
        [sg.Text(f'Hora da Saída:')],
        [sg.Text(f'Tempo total em minutos:')],
        [sg.Text(f'Total a pagar:')],
        [sg.Button('Pagar')]
    ]
    
    coluna_direita =[
        [sg.Input(codigo, disabled=True, size=17, text_color='red', font=('Arial', '10', 'bold'), justification='right')],
        [sg.Input(entrada, disabled=True, size=17)],
        [sg.Input(saida, disabled=True, key='txtSaida', size=17)],
        [sg.Input(tempo, disabled=True, size=17, justification='right')],
        [sg.Input(pagar, disabled=True, key='txtPagar',size=17, font=('Arial', '10', 'bold'),justification='right')],
        [sg.Button('Sair')]
    ]    
    
    layout = [
        [sg.Column(coluna_esqueda), sg.Column(coluna_direita, element_justification='rigth')]        
    ]

    window = sg.Window('Pagamento', layout, modal=True)

    while True:
        events, values = window.read()
        if events in (sg.WIN_CLOSED, 'Sair'):
            break
    window.close()