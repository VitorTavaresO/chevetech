from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()
from kivymd.app import MDApp

import managers

from classes.main import MainScreen
from classes.radio import RadioScreen
from classes.smartphone import SmartphoneScreen
from classes.vehicle import VehicleScreen
from classes.location import LocationScreen
from classes.files import FilesScreen
from classes.settings import SettingsScreen
from classes.settings import HotspotScreen


class App(MDApp):
    def build(self):
        self.root = Builder.load_file('view/interface.kv')
        return self.root

    def on_start(self):
       managers.screen_manager = self.root

if __name__ == "__main__":
    App().run()