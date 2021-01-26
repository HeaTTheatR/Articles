from kivy import Config
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'keyboard_mode', 'dock')

from kivy.core.window import Window
Window.size = (420, 720)
Window.minimum_width, Window.minimum_height = Window.size

from kivymd.app import MDApp

from check_screen import CheckScreen


class CheckApplication(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.primary_hue = "100"
        self.screen = CheckScreen()
        return self.screen

    def on_start(self):
        self.screen.dispatch("on_enter")


CheckApplication().run()
