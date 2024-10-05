from flask import Flask, request, send_file, render_template, redirect

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Привіт! Це другий урок по фреймовку Flask"

@app.route("/users/<int:user_id>")
def get_username(user_id):
    return f'Hello {user_id}'

@app.route("/login", methods=['POST'])
def enter_user_data():
    if request.method == 'POST':
        name = request.form['name']
        print(request.form)
        return {'message': name}


@app.route("/register", methods=['POST'])
def user_register():
    if request.method == 'POST':
        data = request.json
        email = data['email']
        password = data['password']
        first_name = data['first_name']

        if len(password) < 8:
            return {'message': 'Твій пароль надто короткий'}
        return {'email': email, 'password': password, 'first_name': first_name}


@app.route("/redirect")
def redirect_route():
    return redirect('https://www.google.com/')

if __name__ == '__main__':
    app.run(debug=True)
