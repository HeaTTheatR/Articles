import os

from kivy.lang import Builder

from kivymd.app import MDApp

from uix.screens.star_screen.baseclass.start_screen import StarAppScreen


class StarTest(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.KV_DIR = os.path.join(self.directory, "uix", "screens")
        self.load_all_kv_files()
        self.screen = StarAppScreen()

    def build(self):
        return self.screen

    def load_all_kv_files(self):
        for dir, dirs, files in os.walk(self.KV_DIR):
            for file in files:
                if file.endswith(".kv"):
                    path = os.path.join(dir, file)
                    with open(path, encoding="utf-8") as kv:
                        Builder.load_string(kv.read())

    def on_start(self):
        self.screen.dispatch("on_enter")


StarTest().run()
