from utilerias.utilss import *

app = Flask(__name__)
api = Api(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Cascaron Servicios',
        version='v1.0',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

app.config["JWTSECRETKEY"] = "super-secret"
jwt = JWTManager(app)


api.add_resource(TodoA, '/api/cascaron')
docs.register(TodoA)



# Crea una ruta para autenticar a los usuarios y devolver el token JWT.
# La función create_access_token() se utiliza para generar el JWT.
@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    id = 135
    # Consulta la base de datos por el nombre de usuario y la contraseña
    
    if username != "Admin" and password != "Inf@1$20":
          # el usuario no se encontró en la base de datos
        return jsonify({"msg": "Bad username or password"}), 401
    
    # crea un nuevo token con el id de usuario dentro
    access_token = create_access_token(identity=id)
    return jsonify({ "token": access_token, "user_id": id })

if __name__ == '__main__':
    app.run(debug=True)