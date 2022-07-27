class consultas_sql:  
    def __init__(self,tabla,db):
        self.tabla = tabla 
        self.db = db  
                            
    # Busqueda                                           
    def busqueda_bd(self,nombre1,apellido1,nombre2,apellido2):
        
        b = self.db.execute("select * from tabla where nombre1 = :nombre1 and nombre2 = :nombre2 and apellido1 = :apellido1 and apellido2 = :apellido2 ",
        {"nombre1":nombre1,"nombre2":nombre2,"apellido1":apellido1,"apellido2":apellido2}).fetchall()  
        
        return b   
        
        