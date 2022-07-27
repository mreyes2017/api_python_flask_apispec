from utilerias.utilss import *

class CASCARONRequestSchema(Schema):
    nombre1 = fields.String(required=True, description="Primer Nombre")
    nombre2 = fields.String(required=False, description="Segundo Nombre")
    apellido1 = fields.String(required=True, description="Primer Apellido")
    apellido2 = fields.String(required=False, description="Segundo Apellido")

class TodoA(MethodResource, Resource):
    @doc(description='Ejemplo de una api REST con flask_restful y apispec.', tags=['CASCARON'])
    @use_kwargs(CASCARONRequestSchema, location=('json'))
    def post(self, **kwargs):
        nombre1 = kwargs.get("nombre1")
        nombre2 = kwargs.get("nombre2")
        apellido1 = kwargs.get("apellido1")
        apellido2 = kwargs.get("apellido2")
     
        lista = {
            "mensaje": f"Bienvenido al mundo de las apis {nombre1} {nombre2} {apellido1} {apellido2} :D ",
            "nombre1": nombre1,
            "nombre2": nombre2,
            "apellido1": apellido1,
            "apellido2": apellido2
            
        }
        
        
        return lista
  
        

            
    