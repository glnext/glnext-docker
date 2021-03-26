import io

import glnext
import numpy as np
from PIL import Image

from flask import Flask, Response

app = Flask(__name__)

instance = glnext.instance()
task = instance.task()

framebuffer = task.framebuffer((512, 512))

pipeline = framebuffer.render(
    vertex_shader=open('vertex_shader.spv', 'rb').read(),
    fragment_shader=open('fragment_shader.spv', 'rb').read(),
    vertex_count=3,
    instance_format='2f',
    instance_count=1000,
)

group = instance.group(buffer=8000 + 4 * 512 * 512)


@app.route('/')
def hello_world():
    return Response('<img src="/random.png">', mimetype='text/html')


@app.route('/random.png')
def random_image():
    with group:
        pipeline.update(instance_buffer=np.random.uniform(-1.0, 1.0, (1000, 2)).astype('f4').tobytes())
        task.run()
        framebuffer.output[0].read()

    buf = io.BytesIO()
    data = group.output[0]
    Image.frombuffer('RGBA', framebuffer.size, data, 'raw', 'RGBA', 0, -1).save(buf, 'PNG')
    return Response(buf.getvalue(), mimetype='image/png')
