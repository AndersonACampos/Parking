import sys
import os
import PySimpleGUI as sg
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb

def cadastrar():
    coluna_esquerda = [
        [sg.Text('Placa:')],
        [sg.Text('Carro:')],
        [sg.Text('Cor:')],
        [sg.Button('Cadastrar')]
    ]

    coluna_direita = [
        [sg.Input(key='txtPlaca', size=20)],
        [sg.Input(key='txtCarro', size=20)],
        [sg.Input(key='txtCor', size=20)],
        [sg.Button('Sair')]
    ]

    layout = [
        [sg.Column(coluna_esquerda), sg.Column(coluna_direita, element_justification='right')]    
    ]

    window = sg.Window('Ticket', layout, modal=True)

    while True:
        events, values = window.read()
        if events in(sg.WIN_CLOSED, 'Sair'):
            break
        if events == 'Cadastrar':
            placa = values['txtPlaca']
            carro = values['txtCarro']
            cor = values['txtCor']
            try:
                tb.cadastrar(placa, carro, cor)
                break
            except Exception as ex:
                sg.popup_error(ex)
            
    window.close()