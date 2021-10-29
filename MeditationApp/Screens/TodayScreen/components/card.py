from kivy.properties import StringProperty

from kivymd.uix.card import MDCard


class CardToday(MDCard):
    icon = StringProperty("play-circle-outline")
    text = StringProperty()
