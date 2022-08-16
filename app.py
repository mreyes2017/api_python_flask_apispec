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

app.config["JWT_SECRET_KEY"] = "super-secret" 
#app.config["JWT_ALGORITHM"] = "HS256"
jwt = JWTManager(app)


api.add_resource(TodoA, '/api/cascaron')
api.add_resource(TodoJWT, '/api/jwt')
docs.register(TodoA)
docs.register(TodoJWT)


if __name__ == '__main__':
    app.run(debug=True)