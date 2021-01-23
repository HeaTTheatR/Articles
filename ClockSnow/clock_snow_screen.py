import os

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size

from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import CircularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout


class ClockSnowScreen(MDScreen):
    shift_celsius_box = NumericProperty(0)

    def start_animation_snowflake_bg(self, interval):
        Animation(scale=1, t="out_elastic", d=1.4).start(self.ids.snowflake_bg)

    def start_animation_snowflake(self, interval):
        Animation(scale=1, t="out_elastic", d=1.4).start(self.ids.snowflake)

    def start_animation_temperature_label(self, interval):
        Animation(scale=1, t="out_back", d=0.2).start(self.ids.temperature_label)

    def start_animation_city_label(self, interval):
        Animation(scale=1, t="out_back", d=0.2).start(self.ids.city_label)

    def start_animation_celsius_box(self, interval):
        Animation(shift_celsius_box=60, t="out_back", d=1.2).start(self)
        Animation(scale=1, t="out_elastic", d=1.2).start(self.ids.temperature_celsius_box)


class RoundShadowBox(CircularElevationBehavior, MDFloatLayout):
    pass


class SnowFlakeBg(MDFloatLayout):
    scale = NumericProperty(0)


Builder.load_file(os.path.join(os.path.dirname(__file__), "clock_snow_screen.kv"))
