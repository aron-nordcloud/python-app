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

<div style="text-align:center; font-size:48px; font-family:Arial; padding:20px; background:#333; color:#fff; border-radius:10px;">
    <div id="clock">{datetime.datetime.now().strftime("%I:%M:%S %p")}</div>
    <div style="font-size:16px; margin-top:10px;">{datetime.datetime.now().strftime("%A, %B %d, %Y")}</div>
</div>
<script>
    function updateClock() {{
        const now = new Date();
        const timeString = now.toLocaleTimeString('en-US', {{ 
            hour12: true, 
            hour: '2-digit', 
            minute: '2-digit', 
            second: '2-digit' 
        }});
        const dateString = now.toLocaleDateString('en-US', {{ 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        }});
        
        document.getElementById('clock').innerHTML = timeString;
        document.getElementById('date').innerHTML = dateString;
    }}
    
    setInterval(updateClock, 1000);
    updateClock();
</script>

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
