from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_dojo import Dojo


db = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
    @classmethod
    def addninja(cls,data):
        query = """
        INSERT into ninjas (first_name,last_name,age,dojo_id)
        Values (%(first_name)s, %(last_name)s, %(age)s , %(dojo_id)s)
        """
        return connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def allninjas(cls):
        query = """
        SELECT * FROM dojos
        Join ninjas
        ON dojos.id = ninjas.dojo_id
        """
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            ninjadojo = cls(dojo)
            dojo_data = {
            'id':dojo['id'],
            'name':dojo['name'],
            'created_at':dojo['created_at'],
            'updated_at':dojo['updated_at']
        }
            ninjadojo.master = Dojo(dojo_data)
            dojos.append(ninjadojo)
        return dojos
        
        
        def get_one(cls,data):
            query = """
            SELECT * FROM ninjas
            WHERE dojo_id = %(dojo_id)s
            """
            results = connectToMySQL (db).query_db(query,data)
            return cls(results[0])