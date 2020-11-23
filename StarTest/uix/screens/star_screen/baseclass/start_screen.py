from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class StarAppLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "data/font/nasalization-rg.ttf"
        self.halign = "center"


class StarAppScreen(ThemableBehavior, MDScreen):
    planets = ["mars", "venus", "jupiter", "mercury"]
    animation_back = ObjectProperty(False)

    def on_enter(self, *args):
        for planet in self.planets:
            self.ids.carousel.add_widget(
                StarAppLabel(
                    text=" ".join(list(planet)).upper(),
                    font_size="12sp",
                    pos_hint={"center_y": 0.5},
                    text_color=self.theme_cls.secondary_text_color,
                    bold=True,
                )
            )
        self.ids.planet_img.source = f"data/images/{self.planets[0]}.png"
        self.ids.vertical_lbl.text = self.planets[0].upper()

    def set_planet(self, carousel, index):
        def set_new_planet(*args):
            name_planet = "".join(carousel.slides[index].text.split(" ")).lower()
            self.ids.planet_img.source = f"data/images/{name_planet}.png"
            Animation(
                angle=45,
                size=(dp(100), dp(100)),
                d=0.2,
            ).start(self.ids.planet_img)

        self.ids.vertical_lbl.text = "".join(carousel.slides[index].text.split(" "))
        self.ids.planet_lbl.text = self.ids.vertical_lbl.text
        anim = Animation(
            angle=0,
            size=(0, 0),
            d=0.2,
        )
        anim.bind(on_complete=set_new_planet)
        anim.start(self.ids.planet_img)

    def start_animation(self):
        Animation(
            size=(self.width * 2, self.height * 2),
            d=0.5,
        ).start(self.ids.helmet_img)
        Animation(
            y=0,
            d=1.2,
        ).start(self.ids.shadow_planet_img)
        Animation(
            opacity=0.6,
            d=1.2,
        ).start(self.ids.box_name_planet)
        Animation(
            opacity=0.7,
            size=(dp(150), dp(150)),
            d=0.7,
        ).start(self.ids.earth_img)
        Animation(
            opacity=1,
            d=1.2,
        ).start(self.ids.light_img)
        Animation(
            size=self.size,
            opacity=1,
            d=0.7,
            t="in_sine",
        ).start(self.ids.bg_img)
        Animation(
            angle=45 if not self.ids.planet_img.angle else 0,
            size=(self.width - dp(40), self.width - dp(40)),
            pos_hint={"center_y": 0.05},
            d=1,
            t="in_back",
        ).start(self.ids.planet_img)
        Animation(
            color=(1, 1, 1, 1),
            d=1,
        ).start(self.ids.toolbar)
        Animation(opacity=0, d=0.5).start(self.ids.box_carousel)

        Animation(
            opacity=1,
            y=self.ids.planet_lbl.height
            + self.ids.info_lbl.height
            + self.ids.more_lbl.height
            + dp(24),
            d=0.9,
            t="in_out_back",
        ).start(self.ids.planet_lbl)
        Animation(
            opacity=0.6,
            y=self.ids.info_lbl.height + self.ids.more_lbl.height + dp(24),
            d=1.0,
            t="in_out_back",
        ).start(self.ids.info_lbl)
        Animation(
            opacity=1,
            y=self.ids.more_lbl.height + dp(24),
            d=1.1,
            t="in_out_back",
        ).start(self.ids.more_lbl)
        Animation(
            opacity=1,
            y=self.ids.more_lbl.height + dp(20),
            d=1.2,
            t="in_out_back",
        ).start(self.ids.sep)
        self.animation_back = True

    def back_animation(self):
        Animation(
            size=(dp(250), dp(250)),
            d=0.5,
        ).start(self.ids.helmet_img)
        Animation(
            y=-self.ids.shadow_planet_img.height,
            d=1.2,
        ).start(self.ids.shadow_planet_img)
        Animation(
            opacity=0,
            d=1.2,
        ).start(self.ids.box_name_planet)
        Animation(
            opacity=0,
            size=(0, 0),
            d=0.7,
        ).start(self.ids.earth_img)
        Animation(
            opacity=0,
            d=1.2,
        ).start(self.ids.light_img)
        Animation(
            opacity=0,
            d=0.7,
            t="in_sine",
        ).start(self.ids.bg_img)
        Animation(
            angle=45,
            size=(dp(100), dp(100)),
            pos_hint={"center_y": 0.5},
            d=1,
            t="in_back",
        ).start(self.ids.planet_img)
        Animation(
            color=(0, 0, 0, 1),
            d=1,
        ).start(self.ids.toolbar)
        Animation(opacity=1, d=0.5).start(self.ids.box_carousel)

        Animation(
            opacity=0,
            y=-self.ids.planet_lbl.height,
            d=0.9,
            t="in_out_back",
        ).start(self.ids.planet_lbl)
        Animation(
            opacity=0,
            y=-self.ids.info_lbl.height,
            d=1.0,
            t="in_out_back",
        ).start(self.ids.info_lbl)
        Animation(
            opacity=0,
            y=-self.ids.more_lbl.height,
            d=1.1,
            t="in_out_back",
        ).start(self.ids.more_lbl)
        Animation(
            opacity=0,
            y=self.ids.sep.height,
            d=1.2,
            t="in_out_back",
        ).start(self.ids.sep)
        self.animation_back = False
