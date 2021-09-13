import os
import importlib

from kivy.core.window import Window

from kaki.app import App


class OnBoardScreenAppLive(App):
    KV_FILES = {
        os.path.join(os.getcwd(), "boarding_screen.kv"),
        os.path.join(os.getcwd(), "slide.kv"),
    }
    CLASSES = {
        "BoardScreen": "boarding_screen",
        "Slide": "slide",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        import boarding_screen

        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(boarding_screen)

        return boarding_screen.BoardScreen()

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()


OnBoardScreenAppLive().run()
