import os

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty

Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size

from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    shift_x_email = NumericProperty(0)
    shift_x_password = NumericProperty(0)
    shift_x_signin_button = NumericProperty(0)
    shift_y_authentification_label = NumericProperty(0)
    shift_y_security_label = NumericProperty(0)
    shift_y_authentification_field = NumericProperty(0)
    shift_y_auth_button = NumericProperty(0)
    shift_y_device_label = NumericProperty(0)

    def animation_hide_signin_button(self, interval):
        Animation(
            shift_x_signin_button=self.width,
            d=1.2,
            t="in_back",
        ).start(self)
        Animation(opacity=0, d=1.2).start(self.ids.signin_button)

    def animation_avatar(self):
        Animation(scale=.6, d=1.2).start(self.ids.avatar)

    def animation_hide_email_widgets(self):
        Animation(opacity=0, d=1.2).start(self.ids.email_label)
        Animation(
            shift_x_email=self.width,
            d=1.2,
            t="in_back"
        ).start(self)

    def animation_hide_password_widgets(self, interval):
        Animation(opacity=0, d=1.2).start(self.ids.password_label)
        Animation(
            shift_x_password=self.width,
            d=1.2,
            t="in_back"
        ).start(self)

    def animation_show_authentification_label(self, interval):
        Animation(opacity=1, d=.8).start(self.ids.authentification_label)
        Animation(
            shift_y_authentification_label=dp(56),
            d=.8,
            t="out_back"
        ).start(self)

    def animation_show_security_label(self, interval):
        Animation(opacity=1, d=.8).start(self.ids.security_label)
        Animation(
            shift_y_security_label=dp(12),
            d=.8,
            t="out_back"
        ).start(self)

    def animation_show_authentification_field(self, interval):
        Animation(opacity=1, d=.8).start(self.ids.authentification_field)
        Animation(
            shift_y_authentification_field=dp(24),
            d=.8,
            t="out_back"
        ).start(self)

    def animation_show_auth_button(self, interval):
        Animation(opacity=1, d=.8).start(self.ids.auth_button)
        Animation(
            shift_y_auth_button=dp(24),
            d=.8,
            t="out_back"
        ).start(self)

    def animation_show_device_label(self, interval):
        Animation(opacity=1, d=.8).start(self.ids.lost_device_label)
        Animation(
            shift_y_device_label=dp(12),
            d=.8,
            t="out_back"
        ).start(self)



Builder.load_file(os.path.join(os.path.dirname(__file__), "login_screen.kv"))
