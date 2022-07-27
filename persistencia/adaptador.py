from persistencia.conexion import *
# Configuracion conexion base de datos sql
"""
    1-SQL SERVER
    2-POSTGRES SQL
    class (tipo,usuario,contrasena,host,namebd)
""" 
class EntradaBd():
    def base_Sql(self):
        conexion = Database()
        db = conexion.name_engine(1,"","","","")
        return db
    
