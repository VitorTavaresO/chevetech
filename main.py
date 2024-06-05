import os
import sys
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.config import Config
from kivymd.app import MDApp
from kivy.clock import Clock
from datetime import datetime

# Defina o tamanho da janela antes de importar qualquer coisa do Kivy
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)  # Torne a janela não redimensionável
Config.write()

class App(MDApp):
    def build(self):
        self.screen = Builder.load_file("interface.kv")
        Clock.schedule_interval(self.update_time, 1)
        return self.screen

    def update_time(self, *args):
        now = datetime.now()
        current_time = now.strftime("%H:%M\n%d/%m/%Y")
        self.screen.ids.datetime_label.text = current_time

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    
    App().run()
