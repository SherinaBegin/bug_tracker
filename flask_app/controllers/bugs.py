from crypt import methods
from flask import render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_app.models.bug import Bug

# CREATE


@app.route('/bugs/new/project/<int:project_id>')
def view_bug(project_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    project_data = {
        'id': project_id
    }
    project_id = Project.get_one_project(project_data)
    return render_template('create_bug.html', project=project_data, user=User.get_user_by_id(data), users=User.get_all_users())


@app.route('/bugs/create', methods=['POST'])
def create_bug():
    if 'user_id' not in session:
        return redirect('/logout')
    Bug.create_bug(request.form)
    return redirect('/dashboard')

# READ


@app.route('/bugs/view/<int:bug_id>')
def bug_details(bug_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': bug_id
    }
    bug_data = Bug.get_one_bug(data)
    return render_template('view_bug.html', bug=bug_data, users=User.get_all_users())
# UPDATE


@app.route('/bugs/edit/<int:bug_id>')
def bug_edit(bug_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': bug_id
    }
    bug_data = Bug.get_one_bug(data)
    return render_template('update_bug.html', bug=bug_data, users=User.get_all_users())


@app.route('/bugs/update/<int:bug_id>', methods=['POST'])
def bug_update(bug_id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Bug.validate_bug(request.form):
        return redirect(f'/bugs/edit/{bug_id}')
    Bug.update_bug(request.form)
    return redirect(f'/bugs/view/{bug_id}')


# DELETE


@app.route('/bugs/delete/<int:bug_id>')
def delete_bug(bug_id):
    data = {
        'id': bug_id
    }
    Bug.destroy_bug(data)
    return redirect('/dashboard')
