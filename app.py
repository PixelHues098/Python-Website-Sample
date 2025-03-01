from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO 2E!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    