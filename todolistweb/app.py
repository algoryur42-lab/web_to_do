from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, title="Мой To-Do List")

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form.get('task_description')
    tasks.append({'description': description, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task_form(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True if request.form.get('completed') else False
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)