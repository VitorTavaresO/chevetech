from kivy.lang import Builder
from kivymd.app import MDApp

class App(MDApp):
    def build(self):
        return Builder.load_file('interface.kv')

App().run()
