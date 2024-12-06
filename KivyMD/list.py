from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from kivymd.uix.label import label
from kivy.core.window import Window
from datetime import datetime
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen  # Importado de kivy.uix.screenmanager
from kivy.uix.screenmanager import SlideTransition

import sys
import os
# Adiciona o diretório pai ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import BLL.TicketBLL as tb

# Configura o tamanho da janela
Window.size = (360, 640)  # Altere para simular outro dispositivo

class MainScreen(Screen):
    def build(self):
        self.theme_cls.theme_style = "Light"
        menu_items = [
        {
            "viewclass": "OneLineListItem",
            "text": f"Item {i}",
            "height": dp(56),
            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        return Builder.load_file('list.kv')

class SecondScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        menu_items = [
        {
            "viewclass": "OneLineListItem",
            "text": f"Item {i}",
            "height": dp(56),
            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        return Builder.load_file('list.kv')

    def on_start(self):
        # Assumindo que tb.buscar_todos() retorna uma lista de tuplas
        tickets, colunas = tb.buscar_todos();
        
        print(colunas)

        for ticket in tickets:
            item = ThreeLineIconListItem(
                text=f"Ticket: {str(ticket[0]).zfill(6)}",
                secondary_text=f"Entrada: {ticket[1][0:16]}",
                tertiary_text=f"{ticket[5]} {ticket[6]} - {ticket[4]}",
            )
            icon = IconLeftWidget(icon="car")
            item.add_widget(icon)
            self.root.get_screen("main").ids.my_list.add_widget(item)
    
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        # Snackbar(text=text_item).open()
        print(text_item)
        
    def change_screen(self):
        self.root.transition = SlideTransition(direction='left')
        self.root.current = "second"  # Navega para a segunda tela

    def change_screen_back(self):
        self.root.transition = SlideTransition(direction='right')
        self.root.current = "main"  # Volta para a tela principal

if __name__ == "__main__":
    MainApp().run()