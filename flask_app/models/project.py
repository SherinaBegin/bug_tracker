from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Project:
    db = 'soloProjectBugTracker'

    def __init__(self, data):
        self.id = data['id']
        self.projectName = data['projectName']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.due_date = data['due_date']

   # CREATE
    @classmethod
    def create_project(cls, data):
        query = """
      INSERT INTO projects (projectName, user_id, due_date)
      VALUES (%(projectName)s, %(user_id)s, %(due_date)s)
      ;"""
        return connectToMySQL(cls.db).query_db(query, data)

   # READ
    @classmethod
    def get_all_projects(cls):
        query = """
      SELECT * FROM projects;
      """
        results = connectToMySQL(cls.db).query_db(query)
        projects = []
        for row in results:
            projects.append(cls(row))
        print(projects)
        return projects

    @classmethod
    def get_one_project(cls, data):
        query = """
      SELECT * FROM projects
      WHERE id = %(id)s
      ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return cls(result[0])

   # UPDATE
    @classmethod
    def update_project(cls, data):
        query = """
        UPDATE projects 
        SET projectName = %(projectName)s,
            due_date = %(due_date)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)
   # DELETE

    @classmethod
    def destroy_project(cls, data):
        query = """
       DELETE FROM projects
       WHERE id = %(id)s
       """
        return connectToMySQL(cls.db).query_db(query, data)

   # VALIDATE PROJECT
    @staticmethod
    def validate_project(project):
        is_valid = True
        if len(project['projectName']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters long")
        if len(project['due_date']) < 6:
            is_valid = False
            flash("Please enter a date")
        return is_valid
