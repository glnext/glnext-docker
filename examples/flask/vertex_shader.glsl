#version 450
#pragma shader_stage(vertex)

layout (location = 0) in vec2 in_pos;
layout (location = 0) out vec4 out_color;

vec2 positions[3] = vec2[](
    vec2(-0.05, -0.05),
    vec2(0.05, -0.05),
    vec2(0.0, 0.05)
);

vec4 colors[3] = vec4[](
    vec4(1.0, 0.0, 0.0, 1.0),
    vec4(0.0, 1.0, 0.0, 1.0),
    vec4(0.0, 0.0, 1.0, 1.0)
);

void main() {
    gl_Position = vec4(positions[gl_VertexIndex] + in_pos, 0.0, 1.0);
    out_color = colors[gl_VertexIndex];
}
