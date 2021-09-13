from kivy.core.window import Animation
from kivy.utils import get_color_from_hex

from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen


class BoardScreen(ThemableBehavior, MDScreen):
    def on_slide_complete(self, instance_carousel):
        for instance_dot in self.ids.box_dots.children:
            if instance_dot.index == instance_carousel.index:
                Animation(
                    md_bg_color=get_color_from_hex("#5ac1c2"), d=0.2
                ).start(instance_dot)
            else:
                Animation(
                    md_bg_color=self.theme_cls.disabled_hint_text_color, d=0.2
                ).start(instance_dot)
