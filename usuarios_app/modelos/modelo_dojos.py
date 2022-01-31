from usuarios_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__( self, id, name, location, languaje, comment, created_at, update_at ):
        self.id = id
        self.name = name
        self.location = location
        self.languaje = languaje
        self.comment = comment
        self.created_at = created_at
        self.update_at = update_at
    
    @classmethod
    def agregaDojo( cls, nuevoDojo ):
        query2 = "ALTER TABLE dojos AUTO_INCREMENT = 1;"
        connectToMySQL( "encuesta_dojo" ).query_db( query2 )
        query = "INSERT INTO dojos(name, location, languaje, comment, created_at, update_at) VALUES(%(name)s, %(location)s, %(languaje)s, %(comment)s, %(created_at)s, %(update_at)s);"
        resultado = connectToMySQL( "encuesta_dojo" ).query_db( query, nuevoDojo )
        return resultado
    
    @classmethod
    def obtenerDojo(cls, encontrarDojo):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s"
        resultado = connectToMySQL( "encuesta_dojo" ).query_db( query, encontrarDojo )
        return resultado