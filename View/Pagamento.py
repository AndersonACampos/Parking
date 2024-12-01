import os
import sys
import PySimpleGUI as sg
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb

def fechar_conta(ticket):
    
    codigo = str(ticket[0]).zfill(6)
    entrada = datetime.strptime( ticket[1],'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
    agora = datetime.now().replace(microsecond=0)
    saida = datetime.strptime( ticket[2],'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S') if ticket[2] != '' else agora.strftime('%d/%m/%Y %H:%M:%S') 
    tempo = tb.calcula_tempo(entrada, saida)
    valor = tb.calcular_valor_pagar(tempo)
    pagar = f"R$ {valor:,.2f}"
    pago = ticket[8]
    
    if pago == 'Sim':
        sg.popup(f'O ticket {codigo} já foi pago.')
    
    coluna_esqueda = [
        [sg.Text(f'Ticket:')],
        [sg.Text(f'Hora da Entrada:')],
        [sg.Text(f'Hora da Saída:')],
        [sg.Text(f'Tempo total em minutos:')],
        [sg.Text(f'Total a pagar:')],
        [sg.Button('Pagar', disabled=False if pago == 'Não' else True)]
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
        
        if events == 'Pagar':
            try:
                tb.pagar(ticket[0], ticket[2] if ticket[2] != '' else agora, tempo, valor)
                sg.popup('Ticket pago')
                break
            except Exception as ex:
                sg.popup_error(ex)          
        
    window.close()