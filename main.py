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
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)



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

    def show_dialog(self):
        self.dialog = MDDialog(
            MDDialogIcon(
                icon="access-point-network",
            ),
            MDDialogHeadlineText(
                text="Alterar Configuração do Hotspot",
            ),
            MDDialogContentContainer(
                MDDivider(),
                MDTextField(
                    MDTextFieldHintText(
                        text= "Nome do Hotspot"
                    ),
                    mode= "outlined",
                ),
                
                MDTextField(
                    MDTextFieldHintText(
                        text= "Senha do Hotspot"
                    ),
                    mode= "outlined",
                ),
                MDDivider(),
                orientation="vertical",
                spacing="12dp",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancelar"),
                    style="text",
                    on_release=self.close_dialog,
                ),
                MDButton(
                    MDButtonText(text="Salvar"),
                    style="text",
                ),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()


class App(MDApp):
    def build(self):
        self.root = Builder.load_file('view/interface.kv')
        return self.root

if __name__ == "__main__":
    App().run()