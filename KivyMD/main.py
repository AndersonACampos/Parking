from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen  # Importado de kivy.uix.screenmanager
from kivy.lang import Builder

KV = '''
ScreenManager:
    MainScreen:
    SecondScreen:

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: "vertical"
        spacing: 20
        padding: 20

        MDRaisedButton:
            text: "Ir para a Segunda Tela"
            size_hint: None, None
            size: "200dp", "50dp"
            on_release: app.change_screen()

<SecondScreen>:
    name: "second"
    BoxLayout:
        orientation: "vertical"
        spacing: 20
        padding: 20

        MDRaisedButton:
            text: "Voltar para a Tela Principal"
            size_hint: None, None
            size: "200dp", "50dp"
            on_release: app.change_screen_back()
'''

class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_screen(self):
        self.root.current = "second"  # Navega para a segunda tela

    def change_screen_back(self):
        self.root.current = "main"  # Volta para a tela principal

MainApp().run()
