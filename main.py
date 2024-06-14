from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDButton
from kivymd.uix.textfield import MDTextField

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_datetime, 1)

    def update_datetime(self, dt):
        self.ids.datetime_label.text = datetime.now().strftime("%H:%M\n%d-%m-%Y")

class RadioScreen(MDScreen):
    pass

class SmartphoneScreen(MDScreen):
    pass

class VehicleScreen(MDScreen):
    pass

class LocationScreen(MDScreen):
    pass

class FilesScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    def toggle_button_text(self, text, button):
        if text.text == "OFF":
            text.text = "ON"
            button.md_bg_color = (0.118, 0.678, 0.298, 1)
        else:
            text.text = "OFF"
            button.md_bg_color = (0.1, 0.1, 0.1, 1)

class HotspotScreen(MDScreen):
    dialog = None

    def show_dialog(self, card_id):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Editar Rede",
                type="custom",
                content_cls=BoxLayout(
                    orientation="vertical",
                    spacing="12dp",
                    size_hint_y=None,
                    height="120dp",
                    children=[
                        MDTextField(
                            id="hotspot_name_field",
                            hint_text="Nome da Rede",
                            text=self.ids.hotspot_name.text
                        ),
                        MDTextField(
                            id="hotspot_password_field",
                            hint_text="Senha da Rede",
                            text=self.ids.hotspot_password.text
                        ),
                    ]
                ),
                buttons=[
                    MDButton(
                        style="elevated",
                        text="CANCEL",
                        on_release=self.close_dialog
                    ),
                    MDButton(
                        style="elevated",
                        text="OK",
                        on_release=lambda *args: self.update_network_info(card_id)
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def update_network_info(self, card_id, *args):
        new_name = self.dialog.content_cls.children[1].text
        new_password = self.dialog.content_cls.children[0].text
        self.ids.hotspot_name.text = new_name
        self.ids.hotspot_password.text = new_password
        self.ids[card_id].children[0].children[1].text = new_name
        self.ids[card_id].children[0].children[3].text = new_password
        self.close_dialog()


class App(MDApp):
    def build(self):
        self.root = Builder.load_file('view/interface.kv')
        return self.root

if __name__ == "__main__":
    App().run()