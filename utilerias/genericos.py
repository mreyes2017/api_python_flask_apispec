from utilerias.utilss import *

import base64




class Genericos:
    
    def lista_vacia(self,todo_id):
            if len(todo_id) == 0:
                return abort(404, message="No se encontro lo solicitado, pruebe con otra variante")
    def error(self):
            return abort(404, message="No se encontro lo solicitado, pruebe con otra variante")
        
    def errorF(self):
            return abort(403, message="Error de tipeo usar este formato: {'cedula':'fields.String'}")
        
    def formato(self,fecha):
            formato = fecha
            ff = formato.strftime("%d/%m/%Y")
            return ff 
def image_to_base64(img):
        encoded = base64.b64encode(bytes(img))
        foto_mostrar = "data:image/png;base64,"+encoded.decode()
        return foto_mostrar
