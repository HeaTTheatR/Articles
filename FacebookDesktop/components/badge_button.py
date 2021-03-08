from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout


class BadgeButton(MDRelativeLayout):
    icon = StringProperty()
    text = StringProperty()
