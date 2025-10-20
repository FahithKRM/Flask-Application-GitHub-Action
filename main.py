from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to Deploy Application"

# app.run(port=5178, debug=True)
