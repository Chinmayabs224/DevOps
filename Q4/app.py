from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # In production, use a WSGI server like gunicorn. 
    # For this demo, the built-in server is fine.
    app.run(host="0.0.0.0", port=5000)
