from utilerias.utilss import *
from flask_jwt_extended import create_access_token

class CASCARON_jwt_RequestSchema(Schema):
    username = fields.String(required=True, description="Usuario")
    password = fields.String(required=True, description="Contraseña")

class TodoJWT(MethodResource, Resource):
    @doc(description='Ejemplo de una api REST con flask_restful y apispec.', tags=['CASCARON'])
    @use_kwargs(CASCARON_jwt_RequestSchema, location=('json'))
    def post(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        id = 135
        if username != "Admin" and password != "123":
            # el usuario no se encontró en la base de datos
            response = jsonify({"msg": "Bad username or password"})
            response.status_code = 401 # or 400 or whatever
            return response
           
    
        # crea un nuevo token con el id de usuario dentro
        access_token = create_access_token(identity=id)
        response = jsonify({ "token": access_token, "user_id": id })
        response.status_code = 200 # or 400 or whatever
        return response
       
  
        

            
    