from flask import Flask, render_template_string

app = Flask(__name__)
BG_COLOR = "#DDF2FF"

def get_version():
    with open("VERSION.txt") as f:
        return f.read().strip()

HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>DevSecOps Demo</title>
    <style>
      body { background-color: {{ bg_color }}; font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
      h1 { color: #333; }
      p { font-size: 1.2em; }
    </style>
  </head>
  <body>
    <h1>Hello, DevSecOps Demo!</h1>
    <p>App Version: {{ version }}</p>
  </body>
</html>
"""

@app.route("/")
def home():
    version = get_version()
    return render_template_string(HTML_TEMPLATE, version=version, bg_color=BG_COLOR)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
