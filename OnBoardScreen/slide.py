from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout


class Slide(MDRelativeLayout):
    source = StringProperty()
    text = StringProperty()
