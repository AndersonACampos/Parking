import sys
import os
import PySimpleGUI as sg
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb
import time

try:
    ticket, colunas = tb.buscar_todos();
except Exception as ex:
    sg.popup_error(ex)

sg.theme('Default1')

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

# Variável para armazenar o tempo do último clique
ultimo_clique = 0

while True:
    event, values = window.read()
    # print(event, values)
    if event in (sg.WINDOW_CLOSED,"cmdFechar") :
        break
    if event == 'grdTickets':
        
        tempo_atual = time.time()
        intervalo = tempo_atual - ultimo_clique
        print(intervalo)
        
        # Verifica se foi um duplo clique (ajustável)
        if intervalo < 4:  # 0.3 segundos entre cliques        
            linhas = values['grdTickets'][0]
            sg.popup(ticket[linhas])
        else:
            # Atualiza o tempo do último clique
            ultimo_clique = tempo_atual
        
window.close()