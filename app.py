import socket
from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/status')
def status():
    return jsonify({'status': 'OK'})


@app.route('/testhtml')
def testhtml():
    return render_template('index.html')

@app.route('/hostdetails')
def hostdetails():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return jsonify({'hostname': hostname, 'hostip': hostip})

if __name__ == '__main__':
    print('Hello World')
    app.run(host='0.0.0.0', port=5001, debug=True)


