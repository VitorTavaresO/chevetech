from kivy.app import App
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

global app
global screen_manager

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
    def toggle_button_text(self, text_field, button):
        if text_field.text == "OFF":
            text_field.text = "ON"
            button.md_bg_color = (0.118, 0.678, 0.298, 1)
        else:
            text_field.text = "OFF"
            button.md_bg_color = (0.1, 0.1, 0.1, 1)

class HotspotScreen(MDScreen):

    def toggle_button_text(self, text_field, button):
        if text_field.text == "OFF":
            text_field.text = "ON"
            button.md_bg_color = (0.118, 0.678, 0.298, 1)
        else:
            text_field.text = "OFF"
            button.md_bg_color = (0.1, 0.1, 0.1, 1)

    dialog = None

    def show_dialog(self):

        self.hotspot_name_input = MDTextField(
            MDTextFieldHintText(
                text="Nome do Hotspot"
            ),
            mode="outlined",
            id="hotspot_name_input"
        )

        self.hotspot_password_input = MDTextField(
            MDTextFieldHintText(
                text="Senha do Hotspot"
            ),
            mode="outlined",
            id="hotspot_password_input"
        )

        self.dialog = MDDialog(
            MDDialogIcon(
                icon="access-point-network",
            ),
            MDDialogHeadlineText(
                text="Alterar Configuração do Hotspot",
            ),
            MDDialogContentContainer(
                MDDivider(),
                self.hotspot_name_input,
                self.hotspot_password_input,
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
                    on_release=self.save_inputs,
                ),
                spacing="8dp",
            ),
        )
        self.dialog.open()
    

    def save_inputs(self, instance):
        screen_manager = App.get_running_app().root

        hotspot_name = self.hotspot_name_input.text
        hotspot_password = self.hotspot_password_input.text

        settings_screen = screen_manager.get_screen('hotspot')

        hotspot_name_label = settings_screen.ids['hotspot_name']
        hotspot_password_label = settings_screen.ids['hotspot_password']
        
        if(hotspot_name != ""):
            hotspot_name_label.text = hotspot_name
        if(hotspot_password != ""):
            hotspot_password_label.text = hotspot_password
        
        self.close_dialog()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class App(MDApp):
    def build(self):
        self.root = Builder.load_file('view/interface.kv')
        return self.root

if __name__ == "__main__":
    App().run()