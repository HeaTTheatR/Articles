from kivy.properties import StringProperty

from FacebookDesktop.components.cards.fake_card import FakeCard


class ChatCard(FakeCard):
    avatar = StringProperty()
    text = StringProperty()
    name = StringProperty()
