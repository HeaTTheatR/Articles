from kivy.config import Config

Config.set("graphics", "window_state", "maximized")

from kivy.core.window import Window

Window.minimum_width, Window.minimum_height = (1200, 600)

from kivymd.app import MDApp

from facebook_desktop import FacebookDesktop


class FacebookDesktopMain(MDApp):
    def build(self):
        return FacebookDesktop()


FacebookDesktopMain().run()
