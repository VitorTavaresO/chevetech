from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from datetime import datetime

class MainScreen(MDScreen):
    pass

class ConfigScreen(MDScreen):
    pass

class App(MDApp):
    def build(self):
        return Builder.load_file("interface.kv")
    
if __name__ == "__main__":
    App().run()