from kivy.animation import Animation
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.boxlayout import MDBoxLayout


class Tab(MDBoxLayout):
    icon = StringProperty()
    active = BooleanProperty(False)

    def on_active(self, instance, value):
        Animation(
            opacity=value,
            width=self.width if value else 0,
            d=0.25,
            t="in_sine" if value else "out_sine",
        ).start(self.ids.separator)
