from flask import Flask, render_template, jsonify
import random
import webbrowser
import socket

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Route für das Würfeln
@app.route('/roll')
def roll_dice():
    dice_roll = random.randint(1, 6)  # Zufallszahl zwischen 1 und 6
    return jsonify(dice_roll=dice_roll)

if __name__ == "__main__":
    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)
    url = f"http://{local_ip}:4999"
    
    print(f"Server läuft! Öffne {url} in deinem Browser.")
    webbrowser.open(url)  # Diese Zeile öffnet die Webseite automatisch
    
    app.run(debug=False, host='0.0.0.0', port=4999)
