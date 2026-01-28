from flask import Flask, jsonify
import datetime
import socket
from os import environ

app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, big human! check cd runners after argocd',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    port = int(environ.get("PORT", 5050))  # default to 5050
    app.run(host='0.0.0.0', port=5050)


