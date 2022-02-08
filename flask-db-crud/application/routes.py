from application import app, db
from application.models import Tasks

@app.route('/add')
def add():
    new_task = Tasks(name="New Task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/view')
def view():
    all_tasks = Tasks.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>"+ task.name
    return tasks_string

@app.route('/change/<name>')
def change(name):
    first_task = Tasks.query.first()
    first_task.name = name
    db.session.commit()
    return first_task.name

@app.route('/delete')
def delete():
    first_task = Tasks.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You have deleted the first task in the database"