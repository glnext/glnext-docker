FROM docker.pkg.github.com/glnext/glnext/glnext:swiftshader
RUN python3 -m pip install -U flask==1.1.2 pillow==8.1.2 numpy==1.20.1 waitress==2.0.0
COPY vertex_shader.glsl fragment_shader.glsl /glsl/
WORKDIR /app/
RUN glslc -O -o vertex_shader.spv /glsl/vertex_shader.glsl &&\
    glslc -O -o fragment_shader.spv /glsl/fragment_shader.glsl
COPY app.py /app/
CMD exec python3 -m waitress --port 5000 app:app
