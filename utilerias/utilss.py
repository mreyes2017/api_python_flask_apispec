from flask import Flask
import os
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask import request,jsonify
from flask_restful import Resource, marshal,reqparse,abort
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from persistencia.conexion import *
from persistencia.adaptador import *
from persistencia.querySql import *
from .genericos import *


from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

# Servicios

from api.cascaronApi import TodoA
from api.jwtApi import TodoJWT


import json
from flask import request,jsonify
from flask_restful import Resource, fields, marshal,reqparse,abort
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


