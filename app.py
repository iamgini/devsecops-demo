from flask import Flask, render_template_string
import hashlib

app = Flask(__name__)
APP_NAME = "DevSecOps Demo"
VERSION_FILE = "VERSION.txt"

# Colors for background rotation
BG_COLORS = ["#DDF2FF", "#FFDDDD", "#DDFFDD", "#FFFFDD"]

def get_version():
    try:
        with open(VERSION_FILE) as f:
            return f.read().strip()
    except FileNotFoundError:
        return "v0.0.0"

def get_bg_color(version):
    # problematic line for bandit test
    # idx = int(hashlib.md5(version.encode()).hexdigest(), 16) % len(BG_COLORS)

    # clean line
    idx = int(hashlib.sha256(version.encode()).hexdigest(), 16) % len(BG_COLORS)

    return BG_COLORS[idx]

HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>{{ app_name }}</title>
    <style>
      body {
        background-color: {{ bg_color }};
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
        transition: background-color 0.5s;
      }
      h1 { color: #333; font-size: 2.5em; }
      p { font-size: 1.2em; }
      .badge {
        display: inline-block;
        padding: 5px 10px;
        background-color: #333;
        color: #fff;
        border-radius: 5px;
        margin-top: 20px;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <h1>{{ app_name }}</h1>
    <p>App Version: {{ version }}</p>
    <div class="badge">Demo</div>
  </body>
</html>
"""

@app.route("/")
def home():
    version = get_version()
    bg_color = get_bg_color(version)
    return render_template_string(HTML_TEMPLATE, version=version, bg_color=bg_color, app_name=APP_NAME)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
