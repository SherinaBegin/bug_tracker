from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Bug:
    db = 'soloProjectBugTracker'

    def __init__(self, data):
        self.id = data['id']
        self.issue = data['issue']
        self.description = data['description']
        self.priorityLeve = data['priorityLevel']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.project_id = data['project_id']
        self.user_id = data['user_id']

    # CREATE
    @classmethod
    def create_bug(cls, data):
        query = """
            INSERT INTO bugs (issue, description, priorityLevel, status, project_id, user_id)
            VALUES (%(issue)s, %(description)s, %(priorityLevel)s, %(status)s, %(project_id)s, %(user_id)s)
            ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    # READ

    @classmethod
    def get_all_bugs(cls):
        query = """
      SELECT * FROM bugs;
      """
        results = connectToMySQL(cls.db).query_db(query)
        bugs = []
        for row in results:
            bugs.append(cls(row))
        print(bugs)
        return bugs

    @classmethod
    def get_one_bug(cls, data):
        query = """
      SELECT * FROM bugs 
      WHERE id = %(id)s
      ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    # UPDATE

    # DELETE
    @classmethod
    def destroy_project(cls, data):
        query = """
       DELETE FROM bugs
       WHERE id = %(id)s
       """
        return connectToMySQL(cls.db).query_db(query, data)
