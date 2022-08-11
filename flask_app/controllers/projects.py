from flask import render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_app.models.bug import Bug


# CREATE
@app.route('/projects/new')
def new_project():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    users = User.get_user_by_id(data)
    return render_template('create.html', user=users)


@app.route('/projects/create', methods=['POST'])
def create_project():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Project.validate_project(request.form):
        return redirect('/projects/new')
    Project.create_project(request.form)
    return redirect('/dashboard')


# READ
@app.route('/projects/view/<int:project_id>')
def view_project(project_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': project_id
    }
    user_data = {
        'id': session['user_id']
    }
   #  # project information
    project_data = Project.get_one_project(data)
    all_bugs = Bug.get_all_bugs()
    return render_template('view_project.html', project=project_data, user=User.get_user_by_id(data), users=User.get_all_users(), bugs=all_bugs)
# UPDATE

# DELETE


@app.route('/projects/delete/<int:id>')
def delete_project(id):
    data = {
        'id': id
    }
    Project.destroy_project(data)
    return redirect('/dashboard')
