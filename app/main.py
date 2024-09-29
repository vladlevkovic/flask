from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users/<int:user_id>")
def get_username(user_id):
    return f'Hello {user_id}'

if __name__ == '__main__':
    app.run(debug=True)
