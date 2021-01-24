from kivy import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.size = (420, 700)
Window.minimum_width, Window.minimum_height = Window.size

from kivymd.app import MDApp

from login_screen import LoginScreen


class LoginApplication(MDApp):
    def build(self):
        return LoginScreen()


LoginApplication().run()
