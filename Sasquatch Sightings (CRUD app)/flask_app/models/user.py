from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import sighting
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "squatch_watch"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.sightings = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        user = []
        for user in results:
            user.append( cls(user) )
        print(user)
        return user

    @classmethod
    def get_sighting_from_user(cls, data):
        query = "SELECT * FROM users LEFT JOIN sightings ON users.id = sightings.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls( results[0] )
        print(results)
        for row in results:
            data = {
                "id" : row["sightings.id"],
                "location" : row["location"],
                "date" : row["date"],
                "amount" : row["amount"],
                "description" : row["description"],
                "created_at": row["sightings.created_at"],
                "updated_at": row["sightings.updated_at"],
                "user_id": row["user_id"]
            }
            user.sightings.append(sighting.Sighting(data))
        return user
            
    @classmethod
    def get_user_email(cls, data):
        query = "Select * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s, NOW(), NOW() );"
        return connectToMySQL(cls.db).query_db(query, data)


    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            flash("Email is already in used. Try Logging in.", "register")
            is_valid = False
        if len(user['first_name']) < 3:
            flash ("First name is Required!", "register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash ("Last name is Required!", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash ("Invalid email address!", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash ("Password must be more than 8 characters", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash ("Password does not match! Try Again!", "register")

        return is_valid