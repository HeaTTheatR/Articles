from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.loader import Loader

from kivy_garden.frostedglass import FrostedGlass  # NOQA

from kivymd.app import MDApp
from kivymd import images_path

from desktop_concept_screen import DesktopConceptScreenView

Loader.loading_image = f"{images_path}transparent.png"


class DesktopConcept(MDApp):
    def build(self):
        Builder.load_file("desktop_concept_screen.kv")
        return DesktopConceptScreenView()

    def on_start(self):
        def on_start(interval):
            self.root.ids.glass.on_size(None, None)
            Window.maximize()

        Clock.schedule_once(on_start, 3)


DesktopConcept().run()
