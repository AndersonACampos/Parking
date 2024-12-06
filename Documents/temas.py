import PySimpleGUI as sg

# Função para alterar o tema dinamicamente
def mudar_tema(window, novo_tema):
    sg.theme(novo_tema)  # Define o novo tema global
    window.close()  # Fecha a janela atual
    criar_nova_janela(novo_tema)  # Cria a janela novamente com o novo tema

# Função para criar a janela
def criar_nova_janela(tema):
    temas_disponiveis = sg.theme_list()  # Obtém a lista de todos os temas
    layout = [
        [sg.Text('Escolha um tema:')],
        [sg.Combo(temas_disponiveis, default_value=tema, size=(30, 6), key='-COMBO_TEMAS-', ),sg.Button('Aplicar')],
        [sg.Table([[1,'Anderson','Campos','21/02/1972',5],[1,'Anderson','Campos','21/02/1972',5],[1,'Anderson','Campos','21/02/1972',5],[1,'Anderson','Campos','21/02/1972',5]],['Codigo', 'Nome', 'Sobrenome', 'Nascimento', 'Idade'])],
        [sg.Button('Fechar')]
    ]
    
    window = sg.Window('Seleção de Tema', layout)   

    while True:
        event, values = window.read()
        

        if event == sg.WIN_CLOSED or event == 'Fechar':
            break
        elif event == 'Aplicar':
            tema_selecionado = values['-COMBO_TEMAS-']
            if tema_selecionado:
                mudar_tema(window, tema_selecionado)  # Aplica o tema selecionado

    window.close()
temas_disponiveis = sg.theme_list()  # Obtém a lista de todos os temas
# Criando a janela inicial com o tema padrão
sg.theme(temas_disponiveis[0])
criar_nova_janela(temas_disponiveis[0])
