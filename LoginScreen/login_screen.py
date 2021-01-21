import os

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty

Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    scale_box_1 = NumericProperty(1)
    scale_box_2 = NumericProperty(1)
    card_x = NumericProperty(0)

    def on_size(self, *args):
        if self.card_x:
            self.card_x = self.ids.box.width - self.ids.box2.width - dp(40)

    def animation_to_right(self):
        def animation_complete(*args):
            self.ids.box2.add_widget(FingerprintBox())
            Animation(scale=1, d=0.1).start(self.ids.box2.children[0])

        self.ids.box2.clear_widgets()
        Animation(scale=1, d=0.3).start(self.ids.fingerprint_enabled_box)
        Animation(scale=0, d=0.3).start(self.ids.start_uding_fingerprint_box)
        animation = Animation(
            card_x=self.ids.box.width - self.ids.box2.width - dp(40),
            d=0.3,
            t="in_out_cubic",
        )
        animation.bind(on_complete=animation_complete)
        animation.start(self)

    def animation_to_left(self):
        def animation_complete(*args):
            self.ids.box2.add_widget(SignInBox())
            Animation(scale=1, d=0.1).start(self.ids.box2.children[0])

        self.ids.box2.clear_widgets()
        Animation(scale=0, d=0.3).start(self.ids.fingerprint_enabled_box)
        Animation(scale=1, d=0.3).start(self.ids.start_uding_fingerprint_box)
        animation = Animation(
            card_x=0,
            d=0.3,
            t="in_out_cubic",
        )
        animation.bind(on_complete=animation_complete)
        animation.start(self)


class ScaleBox(MDBoxLayout):
    scale = NumericProperty(1)


class FingerprintBox(ScaleBox):
    pass


class SignInBox(ScaleBox):
    pass


Builder.load_file(os.path.join(os.path.dirname(__file__), "login_screen.kv"))
