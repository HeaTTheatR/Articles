import os

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class LoginScreen(MDScreen):
    def show_login_screen(self):
        Animation(
            x=-self.ids.signin_screen.width + dp(48), d=0.35
        ).start(self.ids.signin_screen)
        Animation(
            angle=90, scale=0.4, x=-dp(48), d=0.35
        ).start(self.ids.signin_label)
        Animation(x=dp(48), d=0.35).start(self.ids.login_screen)
        Animation(x=-dp(200), d=0.35).start(self.ids.bg_image)
        Animation(
            x=self.center[0] - self.ids.login_label.width / 2,
            y=self.ids.center_box.y - self.ids.login_label.height - dp(56),
            angle=0,
            scale=1,
            d=0.35,
        ).start(self.ids.login_label)

    def show_sign_screen(self):
        Animation(x=0, d=0.35).start(self.ids.signin_screen)
        Animation(x=self.width - dp(48), d=0.35).start(self.ids.login_screen)
        Animation(x=dp(0), d=0.35).start(self.ids.bg_image)
        Animation(
            x=self.width - self.ids.login_label.width / 2 - dp(48 / 2),
            y=self.ids.center_box.y - self.ids.login_label.height - dp(56),
            angle=90,
            scale=0.4,
            d=0.35,
        ).start(self.ids.login_label)
        Animation(
            x=self.center[0] - self.ids.signin_label.width / 2,
            y=self.ids.center_box.y - self.ids.signin_label.height - dp(56),
            angle=0,
            scale=1,
            d=0.35,
        ).start(self.ids.signin_label)


class ScaleLabel(MDLabel):
    angle = NumericProperty(0)
    scale = NumericProperty(1)


Builder.load_file(os.path.join(os.path.dirname(__file__), "login_screen.kv"))
