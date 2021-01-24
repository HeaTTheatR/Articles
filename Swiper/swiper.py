import os

from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiperItem
from kivymd.app import MDApp
from kivymd.utils.fitimage import FitImage

HOME_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(HOME_DIR, "data", "images")


class Swiper(MDScreen):
    cities = {
        "4.png": "New York",
        "2.png": "London",
        "3.png": "Dubai",
        "5.png": "Tokyo",
        "1.png": "Prague",
    }

    def on_enter(self, *args):
        for name_image in os.listdir(IMAGE_DIR):
            if name_image != "0.png":
                path_to_image = os.path.join(IMAGE_DIR, name_image)
                screen = MDScreen(name=name_image)
                screen.add_widget(FitImage(source=path_to_image))
                MDApp.get_running_app().root.ids.manager.add_widget(screen)
                self.ids.swiper.add_widget(
                    ItemSwiper(
                        source=path_to_image, name_city=self.cities[name_image],
                    )
                )


class ItemSwiper(MDSwiperItem):
    source = StringProperty()
    name_city = StringProperty()


Builder.load_file(os.path.join(HOME_DIR, "swiper.kv"))
