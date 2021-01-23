import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size

from kivymd.uix.dialog import BaseDialog
from kivymd.uix.behaviors import CircularElevationBehavior


class AudioWidget(BaseDialog):
    spin_disk_angle = NumericProperty(360)
    progress_value = NumericProperty(0)
    track_seconds = NumericProperty(480)

    def get_timer(self):
        m = self.track_seconds // 60
        s = self.track_seconds - m * 60
        return "%02d:%02d" % (m, s)

    def start_timer(self):
        def set_time(interval):
            self.progress_value += 1
            self.track_seconds -= 1
            self.ids.progress_box.ids.progress_bar.value = self.progress_value
            self.ids.progress_box.ids.track_seconds.text = self.get_timer()

        Clock.schedule_interval(set_time, 1)

    def show_progress_box(self):
        Animation(
            opacity=1,
            y=self.height - dp(12),
            d=0.4,
        ).start(self.ids.progress_box)
        Animation(y=self.ids.disk_box.y + dp(12), d=0.4).start(self.ids.disk_box)

    def hide_progress_box(self):
        Animation(opacity=0, y=0, d=0.4).start(self.ids.progress_box)
        Animation(y=self.height / 2 - dp(12), d=0.4).start(self.ids.disk_box)

    def spin_disk(self, interval):
        self.spin_disk_angle -= 1
        if self.spin_disk_angle == 0:
            self.spin_disk_angle = 360

    def change_bg(self, instance_bg_image, path_to_bg):
        def set_bg(*args):
            instance_bg_image.source = path_to_bg
            Animation(opacity=1, d=0.2).start(instance_bg_image)

        animation = Animation(opacity=0, d=0.2)
        animation.bind(on_complete=set_bg)
        animation.start(instance_bg_image)


class RoundBoxDisk(MDFloatLayout, CircularElevationBehavior):
    pass


Builder.load_file(os.path.join(os.path.dirname(__file__), "audio_widget.kv"))
