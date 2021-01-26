import os

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior

from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import RectangularRippleBehavior


class CheckScreen(MDScreen):
    open_field_box = 0
    increment_width = NumericProperty(0)
    increment_height = NumericProperty(0)

    def on_size(self, *args):
        if self.open_field_box:
            self.ids.signin_button.width = self.width - dp(50)

    def on_enter(self):
        Animation(x=-dp(300), d=30).start(self.ids.bg_image)

    def start_animation(self):
        Animation(opacity=0, d=0.8).start(self.ids.check_box)
        Animation(opacity=0, d=0.8).start(self.ids.point_box)
        Animation(opacity=0, d=0.8).start(self.ids.login_button)
        Animation(opacity=0, d=0.4).start(self.ids.signin_label)
        Animation(opacity=1, d=1.2).start(self.ids.form_label)
        Animation(opacity=1, d=2.2).start(self.ids.already_label)
        Animation(
            opacity=1,
            y=self.height - (self.ids.toolbar_actions.height + dp(20)),
            d=1.4,
            t="out_quart",
        ).start(self.ids.toolbar_actions)
        anim_transform_button = Animation(
            increment_width=self.width - dp(40) - self.ids.signin_button.width,
            increment_height=dp(270),
            d=1.2,
            t="out_quart",
        )
        anim_transform_button.bind(on_progress=self.anim_transform_button_progress)
        anim_transform_button.start(self)
        Animation(
            y=self.height - dp(386),
            d=1.2,
            t="out_quart",
        ).start(self.ids.signin_button)

    def anim_transform_button_progress(self, animation, instance, value):
        def set_focus(*args):
            self.ids.signin_button.children[-2].focus = True

        if value > 0.5 and not self.open_field_box:
            self.open_field_box = True
            height = 14
            duration = 0.8
            pos_x = 82

            for name_field in ["First Name", "Last Name", "Email", "Password"]:
                height += 54
                duration += 0.2
                pos_x -= 10
                field = MDTextField(
                    x=dp(pos_x),
                    hint_text=name_field,
                    size_hint_x=None,
                    y=self.ids.signin_button.height - dp(height),
                    width=self.ids.signin_button.width - dp(72),
                    opacity=0,
                )
                field.color_mode = "accent"
                self.ids.signin_button.add_widget(field)
                animation = Animation(x=dp(36), opacity=1, t="out_quart", d=duration)
                if duration > 1.5:
                    animation.bind(on_complete=set_focus)
                animation.start(field)


class CustomButton(
    MDRelativeLayout,
    RectangularRippleBehavior,
    ButtonBehavior,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [1, 1, 1, 1]
        self.ripple_color = [0.7, 0.7, 0.7, 1]
        self.radius = [8, ]


Builder.load_file(os.path.join(os.path.dirname(__file__), "check_screen.kv"))
