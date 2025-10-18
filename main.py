from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "App"

# app.run(port=5178, debug=True)