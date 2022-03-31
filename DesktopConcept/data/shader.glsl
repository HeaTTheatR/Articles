// Source - https://gist.github.com/tshirtman/284f1bd71da839ada1550c51ec2c91ef

uniform sampler2D mask;
uniform vec2 mask_pos;
uniform vec2 mask_size;
// mode:
// 0: the mask pixel multiply the texture
// 1: the mask pixel substract to the texture
// addition and division don't seem to be of any use
uniform int mode;

vec4 effect(vec4 color, sampler2D texture, vec2 tex_coords, vec2 coords){
    // get the pixel lookup pos in the mask relative to our main texture
    vec2 pos = tex_coords; // - mask_pos * resolution;
    vec2 size = mask_size / resolution;
    if (
        pos.x < 0. || pos.y < 0. ||
        pos.x > 1. || pos.y > 1.
    )
        if (mode == 0)
            return vec4(0.);
        else
            return color;
    if (mode == 0)
        return color * texture2D(mask, pos);
    else
        return color - texture2D(mask, pos);
}