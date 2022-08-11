from crypt import methods
from flask import render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_app.models.bug import Bug

# CREATE


@app.route('/bugs/create', methods=['POST'])
def create_bug():
    if 'user_id' not in session:
        return redirect('/logout')
    # if not Bug.validate_bug(request.form):
    #    data = {
    #      'id': project_id
    #  }
    #    project_data = Project.get_one_project(data)
    #    return redirect('/projects/view/<int:project_id>')
    Bug.create_bug(request.form)
    return redirect('/dashboard')

# READ

# UPDATE

# DELETE
