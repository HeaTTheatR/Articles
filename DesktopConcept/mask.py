# Source - https://gist.github.com/tshirtman/284f1bd71da839ada1550c51ec2c91ef

import os
from pathlib import Path

from kivy.properties import ObjectProperty, OptionProperty, StringProperty
from kivy.uix.effectwidget import AdvancedEffectBase
from kivy.graphics import BindTexture

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.joinpath("data")

with open(os.path.join(DATA_DIR, "shader.glsl"), encoding="utf-8") as shader:
    glsl = shader.read()


class MaskEffect(AdvancedEffectBase):
    mask = ObjectProperty()
    glsl = StringProperty(glsl)
    mode = OptionProperty('multiply', options=['multiply', 'substract'])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mask.bind(
            pos=self.update_mask,
            size=self.update_mask,
        )
        self.bind(mode=self.update_mask)

    def on_fbo(self, *args):
        self.update_mask()

    def update_mask(self, *args):
        with self.fbo:
            BindTexture(
                texture=self.mask.fbo.texture,
                index=1)
        self.uniforms.update({
            'mask': 1,
            'mask_pos': list(self.mask.pos),
            'mask_size': list(self.mask.size),
            'mode': 0 if self.mode == 'multiply' else 1,
        })
