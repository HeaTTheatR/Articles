import ast
import os

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior

from FacebookDesktop.components.cards.chat_card import ChatCard
from FacebookDesktop.components.cards.friend_card import FriendCard
from FacebookDesktop.components.cards.story_card import StoryCard


class FacebookDesktop(ThemableBehavior, MDScreen):
    def set_active_tab(self, instance_tab):
        for widget in self.ids.tab_box.children:
            if issubclass(widget.__class__, MDBoxLayout):
                if widget == instance_tab:
                    widget.active = True
                else:
                    widget.active = False

    def on_enter(self, app_directory):
        self.list_friends(app_directory)
        self.list_story(app_directory)
        self.list_chat(app_directory)

    def list_chat(self, app_directory):
        with open(os.path.join(app_directory, "assets", "chat.json")) as chat_data:
            chat_data = ast.literal_eval(chat_data.read())
            for name_friend in chat_data.keys():
                self.ids.box_chat.add_widget(
                    ChatCard(
                        name=name_friend,
                        avatar=chat_data[name_friend]["avatar"],
                        text=chat_data[name_friend]["text"],
                    )
                )

    def list_story(self, app_directory):
        with open(os.path.join(app_directory, "assets", "story.json")) as story_data:
            story_data = ast.literal_eval(story_data.read())
            for name_friend in story_data.keys():
                self.ids.story_box.add_widget(
                    StoryCard(
                        name=name_friend,
                        avatar=story_data[name_friend]["avatar"],
                        story=story_data[name_friend]["story"],
                    )
                )

    def list_friends(self, app_directory):
        box_data = {
            "friends.json": self.ids.box_friends,
            "friends_suggested.json": self.ids.box_suggested_friends,
        }
        for name_file in box_data.keys():
            with open(os.path.join(app_directory, "assets", name_file)) as friends_data:
                friends_data = ast.literal_eval(friends_data.read())
                for name_friend in friends_data.keys():
                    box_data[name_file].add_widget(
                        FriendCard(
                            name=name_friend,
                            avatar=friends_data[name_friend]["avatar"],
                            online=friends_data[name_friend]["online"],
                        )
                    )
