import io

import glnext
from flask import Flask, Response, request, send_file
from PIL import Image

app = Flask(__name__)

instance = glnext.instance()
task = instance.task()

image = instance.image((1024, 1024), mode='storage')

framebuffer = task.framebuffer(image.size, samples=1, compute=True)

framebuffer.compute(
    compute_shader=open('compute_shader.spv', 'rb').read(),
    compute_count=(1024, 1024, 1),
    bindings=[
        {
            'binding': 0,
            'type': 'storage_image',
            'images': [
                {
                    'image': image,
                }
            ],
        },
        {
            'binding': 1,
            'type': 'storage_image',
            'images': [
                {
                    'image': framebuffer.output[0],
                }
            ],
        },
    ],
)

group = instance.group(buffer=8 * 1024 * 1024)


@app.route('/')
def form():
    return send_file('static/index.html')


@app.route('/process/', methods=['POST'])
def process():
    img = Image.open(io.BytesIO(request.files['image'].read()))
    img = img.convert('RGBA').resize((1024, 1024)).transpose(Image.FLIP_TOP_BOTTOM)

    with group:
        image.write(img.tobytes())
        task.run()
        framebuffer.output[0].read()

    buf = io.BytesIO()
    data = bytes(group.output[0])
    Image.frombuffer('RGBA', framebuffer.size, data, 'raw', 'RGBA', 0, -1).save(buf, 'PNG')
    return Response(buf.getvalue(), mimetype='image/png')
