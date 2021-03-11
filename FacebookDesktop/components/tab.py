from kivy.animation import Animation
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FocusBehavior


class Tab(FocusBehavior, MDBoxLayout):
    icon = StringProperty()
    active = BooleanProperty(False)

    def on_enter(self):
        Window.set_system_cursor("hand")

    def on_leave(self):
        Window.set_system_cursor("arrow")

    def on_active(self, instance, value):
        Animation(
            opacity=value,
            width=self.width if value else 0,
            d=0.25,
            t="in_sine" if value else "out_sine",
        ).start(self.ids.separator)
