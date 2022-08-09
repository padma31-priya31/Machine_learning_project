from flask import Flask, app
app = Flask(__name__)
@app.route('/')
def welcome():
    return "hi all welcome to learning journey"
@app.route('/members')
def members():
    return "welcoming all members gathered here"

if __name__ == "__main__":
    app.run(debug=True)