from flask import Flask, request, send_file, render_template, redirect
from db import get_all_students, add_student
from db_connect import create_db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/users/<int:user_id>")
def get_username(user_id):
    return f'Hello {user_id}'

@app.route("/students")
def get_students_data():
    students = [
        {
            'name': 'Vladislav',
            'score': 90
        },
        {
            'name': 'Ivan',
            'score': 100
        },
        {
            'name': 'Dmytro',
            'score': 84
        },
        {
            'name': 'Yaroslav',
            'score': 95
        }
    ]
    return render_template('students.html', students=students)

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


@app.route("/data")
def user_data():
    users_list = [
        {
            'username': 'user1'
        },
        {
            'username': 'user2'
        },
        {
            'username': 'user3'
        }
    ]
    user_is_admin = True
    return render_template('data.html', users=users_list, admin=user_is_admin)


@app.route("/links")
def all_links():
    links = [
        'https://google.come',
        'https://facebook.com',
        'https://instagram.com',
        'https://mc.com'
    ]
    return render_template('links.html', links=links)


@app.route("/check")
def check_students():
    return render_template('check_students.html')


@app.route("/participant")
def participants():
    students = get_all_students()
    return render_template('participants.html', students=students)

@app.route("/join", methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        add_student(first_name, last_name, age)
    return render_template('join.html')

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
