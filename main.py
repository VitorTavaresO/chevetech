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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_datetime, 1)

    def update_datetime(self, dt):
        self.ids.datetime_label.text = datetime.now().strftime("%H:%M\n%d-%m-%Y")
class ConfigScreen(MDScreen):
    pass

class App(MDApp):
    def build(self):
        self.root = Builder.load_file("interface.kv")
        return self.root
    
if __name__ == "__main__":
    App().run()