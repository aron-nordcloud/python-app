from flask import Flask, jsonify, Response
import datetime
import socket
from os import environ

app = Flask(__name__)





@app.route('/clock')
def clock():
    hostname = socket.gethostname()
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Clock</title>
    <style>
        body {{ margin:0; padding:0; font-family:Arial; }}
    </style>
</head>
<body>

<iframe 
    src="https://free.timeanddate.com/clock/i8vcosp8/n16/tlnl/fn6/fs48/fcfff/tct/pct/ftb/tt0/tw1/tm1/th1/ta1/tb4"
    frameborder="0"
    width="100%"
    height="150"
    style="display:block;">
</iframe>

<div style="text-align:center; padding:20px;">
    <h2>Hostname: {hostname}</h2>
    <p>You are doing great, big human! check cd runners after argocd retry6</p>
</div>

</body>
</html>
"""
    return Response(html, mimetype="text/html")





@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, big human! check cd runners after clock',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    port = int(environ.get("PORT", 5050))  # default to 5050
    app.run(host='0.0.0.0', port=5050)


# test change
