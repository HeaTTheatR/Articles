import os

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import FocusBehavior, FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard


class FacebookDesktop(ThemableBehavior, MDScreen):
    def set_active_tab(self, instance_tab):
        for widget in self.ids.tab_box.children:
            if issubclass(widget.__class__, MDBoxLayout):
                if widget == instance_tab:
                    widget.active = True
                else:
                    widget.active = False


class ChatCard(MDCard, FakeRectangularElevationBehavior):
    pass


class Tab(MDBoxLayout):
    icon = StringProperty()
    owner = ObjectProperty()
    active = BooleanProperty(False)

    def on_active(self, instance, value):
        Animation(opacity=value, d=0.4).start(self.ids.separator)


Builder.load_file(os.path.join(os.path.dirname(__file__), "facebook_desktop.kv"))
