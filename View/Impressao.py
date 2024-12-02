import datetime
import PySimpleGUI as sg

layout = [
    [sg.Multiline(
f"""     Parking S/A
--------------------------------
Tricket: \t0000002
Data: \t{datetime.datetime.now().strftime('%d/%m/%Y\nHora: \t%H:%M')}
Placa: \tFZQ 6815
Veículo: \tCIVIC
Cor: \tPRETO
""", size=(30,20))],
    [sg.Button('Imprimir')]
]

window = sg.Window('Impressão', layout)

while True:
    events, values = window.read()
    if events in(sg.WIN_CLOSED, 'Fechar'):
        break
window.close()