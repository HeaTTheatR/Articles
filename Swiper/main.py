from kivymd.app import MDApp

from swiper import Swiper


class Main(MDApp):
    def build(self):
        return Swiper()

    def on_start(self):
        self.root.dispatch("on_enter")


Main().run()
