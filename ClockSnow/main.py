from kivy.clock import Clock

from kivymd.app import MDApp

from clock_snow_screen import ClockSnowScreen


class ClockSnow(MDApp):
    def build(self):
        return ClockSnowScreen()

    def on_start(self):
        Clock.schedule_once(self.root.start_animation_snowflake_bg, 1)
        Clock.schedule_once(self.root.start_animation_snowflake, 2.2)
        Clock.schedule_once(self.root.start_animation_temperature_label, 3.2)
        Clock.schedule_once(self.root.start_animation_city_label, 3.2)
        Clock.schedule_once(self.root.start_animation_celsius_box, 2.8)


ClockSnow().run()
