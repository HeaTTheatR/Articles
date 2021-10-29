from kivy.properties import StringProperty

from kivymd.uix.card import MDCard


class Card(MDCard):
    source = StringProperty()
    text = StringProperty()
