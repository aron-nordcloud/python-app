from flask import Flask, jsonify
import datetime
import socket
from os import environ

app = Flask(__name__)



@app.route('/clock')
def clock():
    hostname = socket.gethostname()
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Clock</title>
  <style>
    body { margin:0; padding:0; font-family: Arial, sans-serif; }
    .wrap { display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; }
    .clock { font-size: 64px; font-weight: 600; letter-spacing: 2px; }
    .sub   { margin-top: 16px; color:#444; }
  </style>
</head>
<body>
  <div class="wrap">
    <div id="clock" class="clock">--:--:--</div>
    <h2>Hostname: {{ hostname }}</h2>
    <p class="sub">You are doing great, big human! check cd runners after argocd retry6</p>
  </div>
  <script>
    const opts = { hour: '2-digit', minute: '2-digit', second: '2-digit',
                   hour12: false, timeZone: 'Europe/Amsterdam' };
    function tick() {
      document.getElementById('clock').textContent =
        new Intl.DateTimeFormat(undefined, opts).format(new Date());
    }
    tick(); setInterval(tick, 1000);
  </script>
</body>
</html>
""", hostname=hostname)



@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, big human! check cd runners after argocd retry6',
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
