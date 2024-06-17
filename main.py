from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()
from kivymd.app import MDApp

from models.main import MainScreen
from models.radio import RadioScreen
from models.smartphone import SmartphoneScreen
from models.vehicle import VehicleScreen
from models.location import LocationScreen
from models.files import FilesScreen
from models.settings import SettingsScreen
from models.settings import HotspotScreen


class App(MDApp):
    def build(self):
        self.root = Builder.load_file('view/interface.kv')
        return self.root

if __name__ == "__main__":
    App().run()