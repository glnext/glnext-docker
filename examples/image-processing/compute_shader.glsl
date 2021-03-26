#version 450
#pragma shader_stage(compute)

layout (binding = 0, rgba8) uniform image2D Input;
layout (binding = 1, rgba8) uniform image2D Result;

void main() {
    vec2 pos = vec2(gl_GlobalInvocationID.xy) / 800.0;
    vec3 color = vec3(sin(pos.x), sin(pos.y), cos(pos.x + pos.y));
    ivec2 xy = ivec2(gl_GlobalInvocationID.xy);
    imageStore(Result, xy, imageLoad(Input, xy) * vec4(color, 1.0));
}
