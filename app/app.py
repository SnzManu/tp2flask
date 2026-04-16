from flask import Flask, request, render_template_string
import yaml, subprocess
app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY")
DB_PASSWORD = "admin123"
@app.route("/")
def index():
    return "Hello — vulnerable Flask template for TP2"
@app.route("/parse", methods=["POST"])
def parse():
    data = request.form.get("data", "")
    obj = yaml.safe_load(data)
    return str(obj)
@app.route("/render")
def render():
    name = request.args.get("name", "world")
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)
@app.route("/exec")
def execute():
    host = request.args.get("host", "localhost")
    return subprocess.check_output(["ping", "-c", "1", host])
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
