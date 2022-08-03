from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.password = data['password']

    @classmethod
    def saveUser(cls, data):
        query = 'INSERT INTO users (email, firstName, lastName, password) VALUES (%(email)s, %(firstName)s, %(lastName)s, %(password)s);'
        return connectToMySQL('user_information').query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('user_information').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('user_information').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_all_users(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('user_information').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('user_information').query_db(query, user)
        if len(results) >= 1:
            flash('email is already taken')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if len(user['firstName']) < 1:
            is_valid = False
            flash("First name cannot be blank.")
        if len(user['lastName']) < 1:
            is_valid = False
            flash("Last name cannot be blank.")
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be atleast 8 characters long.")
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash('Passwords do no match.')
        return is_valid
