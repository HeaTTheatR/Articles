from kivymd.app import MDApp

from login_screen import LoginScreen


class LoginApplication(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "Orange"
        return LoginScreen()


LoginApplication().run()
