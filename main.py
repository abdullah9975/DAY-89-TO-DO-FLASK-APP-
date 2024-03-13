from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
# @app.route("/")
# def home():
#     result = db.session.execute(db.select(Task))
#     tasks = result.scalars().all()
#     '''one line of code for the above code to fetch the data from database'''
#     # all_cafes = Cafe.query.all()
#     return render_template("index.html", tasks=tasks, current_user=current_user)


@app.route('/add', methods=['POST'])
def add_task():
    content = request.form.get('task')
    if content:
        new_task = Task(content=content)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')
    else:
        flash('Task content cannot be empty', 'error')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
