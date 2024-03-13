from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample to-do list
todo_list = []


@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo_list.append(task)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete(task_id):
    del todo_list[task_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
