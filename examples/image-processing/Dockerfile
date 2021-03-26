FROM docker.pkg.github.com/glnext/glnext/glnext:swiftshader
RUN python3 -m pip install -U flask==1.1.2 pillow==8.1.2 waitress==2.0.0
COPY compute_shader.glsl /glsl/
WORKDIR /app/
RUN glslc -O -o compute_shader.spv /glsl/compute_shader.glsl
COPY static /app/static
COPY app.py /app/
CMD exec python3 -m waitress --port $PORT app:app
