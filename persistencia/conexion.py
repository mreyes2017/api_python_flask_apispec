from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class Database:

    def name_engine(self,tipo,usuario,contrasena,host,name):
        """
        1-sqlServer
        2-psql
        """ 
        dic_conexiones={
            1:"mssql+pymssql:",
            2:"postgresql:"
        }

        conn =  f"{dic_conexiones[tipo]}"+"//"+f"{usuario}"+":"+f"{contrasena}"+"@"+f"{host}"+"/"+f"{name}"
        #print(conn)
        engine = create_engine(conn)
        db = scoped_session(sessionmaker(bind=engine))
        return db
    
    def error(self):
	    print('error')
        