from kivy.core.window import Window
from kivy.properties import StringProperty

from FacebookDesktop.components.cards.fake_card import FakeCard


class ChatCard(FakeCard):
    avatar = StringProperty()
    text = StringProperty()
    name = StringProperty()

    def on_enter(self):
        Window.set_system_cursor("hand")

    def on_leave(self):
        Window.set_system_cursor("arrow")
