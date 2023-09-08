from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user



class Sighting:
    db = "squatch_watch"
    
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.date = data['date']
        self.amount = data['amount']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.posted_by = None
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings JOIN users on users.id = sightings.user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        sightings = []

        for result in results:
            sighting = cls(result)
            sighting.posted_by = user.User(
                {
                    "id" : result["users.id"],
                    "first_name" : result["first_name"],
                    "last_name" : result["last_name"],
                    "email" : result["email"],
                    "password" : result["password"],
                    "created_at" : result["users.created_at"],
                    "updated_at" : result["users.updated_at"]
                }
            )
            sightings.append(sighting)
        return sightings

    @classmethod
    def save(cls, data):
        query = "INSERT INTO sightings ( location , date , amount , description , user_id , created_at , updated_at ) VALUES ( %(location)s, %(date)s, %(amount)s, %(description)s, %(user_id)s, NOW(), NOW() );"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location = %(location)s, date = %(date)s, amount = %(amount)s, description = %(description)s, updated_at = NOW() WHERE ID = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sightings WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_sighting_by_id(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(id)s ;"
        results = connectToMySQL(cls.db).query_db(query, data)
        sighting = cls( results[0] )
        old_data = results[0]
        data = {
            "id" : old_data["id"],
            "location" : old_data["location"],
            "date" : old_data["date"],
            "amount" : old_data["amount"],
            "description" : old_data["description"],
            "created_at" : old_data["created_at"],
            "updated_at" : old_data["updated_at"],
            "user_id" : old_data['user_id']
        }
        sighting.posted_by = Sighting(data)
        return sighting

    @classmethod
    def get_sighting_with_user(cls, data):
        query = "SELECT * FROM users LEFT JOIN sightings ON users.id = sightings.user_id WHERE sightings.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        sighting = cls( results[0] )
        old_data = results[0]
        data = {
            "id" : old_data["id"],
            "first_name" : old_data["first_name"],
            "last_name" : old_data["last_name"],
            "email" : old_data["email"],
            "password" : old_data["password"],
            "created_at" : old_data["created_at"],
            "updated_at" : old_data["updated_at"]
        }
        sighting.posted_by = user.User(data)
        return sighting

    @staticmethod
    def validate_sighting(sighting):
        is_sighting_valid = True
        if len(sighting['location']) <= 1:
            flash("location is required", "add")
            is_sighting_valid = False
        if len(sighting['date']) <= 1:
            flash("Sighting date is required", "add")
            is_sighting_valid = False
        if len(sighting['amount']) < 1:
            flash("Number of Sasquatches is required", "add")
            is_sighting_valid = False
        if len(sighting['description']) <= 1:
            flash("Description is required", "add")
            is_sighting_valid = False
        return is_sighting_valid