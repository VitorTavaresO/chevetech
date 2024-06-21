import json
from kivy.app import App
from kivymd.uix.screen import MDScreen
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

import managers

class SettingsScreen(MDScreen):
    def on_enter(self, *args):
        data = managers.read_from_data()
        connection_button = self.ids['connection_toggle_button']
        connection_text = self.ids['connection_toggle_text']
        hotspot_button = self.ids['hotspot_toggle_button']
        hotspot_text = self.ids['hotspot_toggle_text']
        
        if(data['settings_screen']['connections']['status'] == "ON"):
            connection_text.text = "ON"
            connection_button.md_bg_color = (0.118, 0.678, 0.298, 1)
            
        else:
            connection_text.text = "OFF"
            connection_button.md_bg_color = (0.1, 0.1, 0.1, 1)
        
        if(data['settings_screen']['hotspot']['status'] == "ON"):
            hotspot_text.text = "ON"
            hotspot_button.md_bg_color = (0.118, 0.678, 0.298, 1)
        else:
            hotspot_text.text = "OFF"
            hotspot_button.md_bg_color = (0.1, 0.1, 0.1, 1)
        
    def toggle_button_text(self, card_id, button):
        status_map = {
            "connection_card": "connections_status",
            "hotspot_card": "hotspot_status",
        }
        if button._button_text.text == "OFF":
            button._button_text.text = "ON"
            button.md_bg_color = (0.118, 0.678, 0.298, 1)
        else:
            button._button_text.text = "OFF"
            button.md_bg_color = (0.1, 0.1, 0.1, 1)

        if card_id in status_map:
            managers.write_to_data(**{status_map[card_id]: button._button_text.text})

class HotspotScreen(MDScreen):
    def on_enter(self):
        data = managers.read_from_data()
        
        hotspot_button = self.ids['hotspot_toggle_button']
        hotspot_text = self.ids['hotspot_toggle_text']
        hotspot_name_label = self.ids['hotspot_name']
        hotspot_password_label = self.ids['hotspot_password']
        
        if data['settings_screen']['hotspot']['status'] == "ON":
            hotspot_text.text = "ON"
            hotspot_button.md_bg_color = (0.118, 0.678, 0.298, 1)
        else:
            hotspot_text.text = "OFF"
            hotspot_button.md_bg_color = (0.1, 0.1, 0.1, 1)

        hotspot_name_label.text = data['settings_screen']['hotspot']['name']
        hotspot_password_label.text = data['settings_screen']['hotspot']['password']

    def toggle_button_text(self, card_id, button):
        settings_screen = self.manager.get_screen('settings')
        settings_screen.toggle_button_text(card_id, button)

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
        hotspot_name = self.hotspot_name_input.text
        hotspot_password = self.hotspot_password_input.text
        
        if(hotspot_name != ""):
            managers.write_to_data(hotspot_name=hotspot_name)

        if(hotspot_password != ""):
            managers.write_to_data(hotspot_password=hotspot_password)
        
        self.on_enter()
        self.close_dialog()

    def close_dialog(self, *args):
        self.dialog.dismiss()