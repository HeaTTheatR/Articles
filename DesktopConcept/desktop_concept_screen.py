from kivy.properties import NumericProperty, DictProperty
from kivy.utils import get_color_from_hex

from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.templates import RotateWidget


class DesktopConceptScreenView(MDScreen):
    index_slide = NumericProperty(0)
    color_data = DictProperty(
        {
            0: get_color_from_hex("#747474"),
            1: get_color_from_hex("#ffffff"),
            2: get_color_from_hex("#ffffff"),
        }
    )

    def set_index_slide(self):
        if self.index_slide == 2:
            self.index_slide = 0
        else:
            self.index_slide += 1


class VerticalLabel(MDLabel, RotateWidget):
    pass
