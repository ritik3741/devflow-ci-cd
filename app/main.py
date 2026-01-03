from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevFlow app is running successfully on Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
