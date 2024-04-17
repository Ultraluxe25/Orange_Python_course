from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Path to database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Creates an instance of DB


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    introduction = db.Column(db.String(), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    public_date = db.Column(db.Datetime, default=datetime.utcnow)

    def __repl__(self):
        return f'Article: {self.id} - {self.title}'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/news')
def news():
    return render_template('news.html')


# @app.route('/jinja2')
# def jinja2():
#     lst = [1, 2, 3, 4, 5]
#     return render_template('jinja2.html', numbers=lst)


# @app.route('/user/<int:user_id>')
# def blog(user_id):
#     return f'Пользователь: {user_id}'


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
