# https://gist.github.com/quitegreensky/9050acdb0cee666efb161ceaec564a85

from random import randint

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_string(
    """
<SnowItem>
    opacity: 0
    size_hint: None, None

    canvas.before:
        Color:
            rgba: .8, .8, .8, 1
        Ellipse:
            pos: self.pos
            size: self.size
"""
)


class SnowItem(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._update)

    def _update(self, *args):
        (Animation(opacity=1, d=randint(*self.parent.time_before_fade))).start(
            self)


class SnowFall(FloatLayout):
    size_range = ListProperty([dp(5), dp(15)])
    time_range = ListProperty([3, 8])
    speed = ListProperty([4, 15])
    time_before_fade = ListProperty([0, 2])
    number = NumericProperty(50)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._update)

    def add_item(self, count):
        for x in range(count):
            item = SnowItem(
                size=[
                    randint(*self.size_range),
                    randint(*self.size_range)
                ],

                pos=[
                    randint(0, self.width),
                    randint(int(self.height * 0.7), self.height)
                ]
            )
            self.add_widget(item)
            self.start_anim(item)
        return item

    def _update(self, *args):
        self.add_item(self.number)

    def start_anim(self, item):
        target_pos = [randint(0, self.width), 0]
        final_time = randint(*self.time_range)

        speed = randint(*self.time_range)
        anim = Animation(pos=target_pos, d=speed)
        anim.start(item)

        # remove
        Clock.schedule_once(lambda x: self.remove_widget(item), final_time)

        # add new
        Clock.schedule_once(lambda x: self.add_item(1), final_time)

        fade_time = final_time - randint(*self.time_before_fade)
        Clock.schedule_once(lambda x: self._fade_out(item, fade_time),
                            final_time - fade_time)

    def _fade_out(self, item, time):
        anim = Animation(opacity=0, d=time)
        anim.start(item)
