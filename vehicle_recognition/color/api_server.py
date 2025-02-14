import argparse
import io

from flask import Flask, jsonify, request
from PIL import Image

from infer import infer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def image_handler():
    bio = io.BytesIO()
    request.files['image'].save(bio)
    image = Image.open(bio)
    # img = np.frombuffer(bio.getvalue(), dtype='uint8')
    result = infer(image)
    return jsonify({'result': result})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=8769, type=int)
    args = parser.parse_args()
    app.debug = True
    app.run('0.0.0.0', args.port)


if __name__ == "__main__":
    main()
