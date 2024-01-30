from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas_schema'


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        
    @classmethod
    def create(cls,data):
        query = """
        INSERT into dojos (name)
        Values (%(name)s)
        """
        return connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos'    
        results = connectToMySQL (db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(dojo)
        return dojos