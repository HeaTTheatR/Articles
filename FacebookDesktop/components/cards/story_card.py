from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout


class StoryCard(MDRelativeLayout):
    avatar = StringProperty()
    story = StringProperty()
    name = StringProperty()

    def on_parent(self, *args):
        if not self.avatar:
            self.remove_widget(self.ids.avatar)
