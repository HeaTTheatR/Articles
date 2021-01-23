from kivymd.app import MDApp
from kivymd.utils.fitimage import FitImage

from audio_widget import AudioWidget


class ClockSnow(MDApp):
    def build(self):
        self.fit_image = FitImage(source="data/images/and-justice-for-all-bg.jpg")
        return self.fit_image

    def on_start(self):
        audio_widget = AudioWidget()
        audio_widget.open()


ClockSnow().run()
