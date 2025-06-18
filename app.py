# app.py
from flask import Flask, render_template, jsonify   # ✅ lowercase 'flask'
import detector
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")            # ✅ render the HTML file

@app.route("/alerts")
def alerts():
    return jsonify(detector.get_alerts())

if __name__ == "__main__":
    thread = threading.Thread(target=detector.start_sniffing)
    thread.daemon = True
    thread.start()
    app.run(debug=True)
