from flask import Flask, request, render_template_string
import yaml, subprocess
app = Flask(__name__)
SECRET_KEY = "sk_live_dQw4w9WgXcQ_HARDCODED_KEY_DO_NOT_USE"
DB_PASSWORD = "admin123"
@app.route("/")
def index():
    return "Hello — vulnerable Flask template for TP2"
@app.route("/parse", methods=["POST"])
def parse():
    data = request.form.get("data", "")
    obj = yaml.load(data, Loader=yaml.Loader)
    return str(obj)
@app.route("/render")
def render():
    name = request.args.get("name", "world")
    return render_template_string(f"<h1>Hello {name}</h1>")
@app.route("/exec")
def execute():
    host = request.args.get("host", "localhost")
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
