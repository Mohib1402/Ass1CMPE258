from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello from Roo!"

if __name__ == "__app__":
    app.run(debug=True)
