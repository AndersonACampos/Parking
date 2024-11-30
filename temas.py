import PySimpleGUI as sg

# Listar todos os temas disponíveis
temas = sg.theme_list()

# Criar uma interface simples para exibir os temas
layout = [
    [sg.Text('Temas disponíveis:')],
    [sg.Listbox(values=temas, size=(30, 20), key='-THEME-LIST-')],
    [sg.Button('Aplicar Tema'), sg.Button('Sair')]
]

janela = sg.Window('Lista de Temas do PySimpleGUI', layout)

# Loop principal
while True:
    evento, valores = janela.read()
    
    # Fechar a janela
    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break
    
    # Aplicar o tema selecionado
    if evento == 'Aplicar Tema':
        tema_selecionado = valores['-THEME-LIST-']
        if tema_selecionado:
            sg.theme(tema_selecionado[0])  # Aplica o tema selecionado
            sg.popup(f'Tema "{tema_selecionado[0]}" aplicado!', title='Tema Aplicado')

janela.close()
