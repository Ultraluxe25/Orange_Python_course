from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/jinja2')
def jinja2():
    lst = [1, 2, 3, 4, 5]
    return render_template('jinja2.html', numbers=lst)


# @app.route('/user/<int:user_id>')
# def blog(user_id):
#     return f'Пользователь: {user_id}'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
