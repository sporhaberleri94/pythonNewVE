from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/status')
def status():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    print('Hello World')
    app.run(host='0.0.0.0', port=5000, debug=True)


