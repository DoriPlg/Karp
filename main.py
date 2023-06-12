from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<MenuScreen>:
    MDBoxLayout:
        MDFlatButton:
            font_size: 40
            text: 'Goto settings'
            on_press: root.switch_to_settings_screen()
        MDFlatButton:
            font_size: 40
            text: 'Quit'

<SettingsScreen>:
    MDBoxLayout:
        MDFlatButton:
            font_size: 40
            text: 'My settings button'
        MDFlatButton:
            font_size: 40
            text: 'Back to menu'
            on_press: root.switch_to_menu_screen()



<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "source/Karpoolz Logo 300X300.jpg"

    MDLabel:
        text: "Karpoolz"
        font_style: "Button"
        adaptive_height: True

    ScrollView:

        DrawerList:
            id: md_list



MDScreen:

    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            MDScreen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Navigation"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget: 
                        id: manager

                        MenuScreen:
                            name: "menu_screen"

                        SettingsScreen:
                            name: "settings_screen"



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''



class ContentNavigationDrawer(MDBoxLayout):
    pass

class MenuScreen(MDScreen):
    def switch_to_settings_screen(self):
        screen_manager = self.parent.parent  # Access the MDScreenManager
        screen_manager.current = "settings_screen"

class SettingsScreen(MDScreen):
    def switch_to_menu_screen(self):
        screen_manager = self.parent.parent  # Access the MDScreenManager
        screen_manager.current = "menu_screen"


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Karpoolz(MDApp):
    def build(self):
        kv = Builder.load_string(KV)
        sm = kv.ids.screen_manager
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(SettingsScreen(name='settings_screen'))
        return kv

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

if __name__ == '__main__':
    Karpoolz().run()