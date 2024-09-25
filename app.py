from flask import Flask, request, jsonify
from seleniumtest import run_selenium_script
from serverless_wsgi import handle_request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def run_selenium():
    data = request.get_json()
    input_numbers = data['input_numbers']
    results = run_selenium_script(input_numbers)
    return jsonify({'results': results})


def handler(event, context):
    return handle_request(app, event, context)

if __name__ == '__main__':
    app.run(host='0.0.0.0')