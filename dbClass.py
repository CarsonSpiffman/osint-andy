from tinydb import TinyDB, Query

class dbGuardar():
    def __init__(self, usuario: str, uuid: str) -> None:
        self.usuario = usuario
        self.UUID = uuid
        self.DB = TinyDB(f'{usuario}_{self.UUID}.json')
        self.query = Query()
        
    def guardarResultados(self, usuario: str, sitio: str, status: str, UID: str) -> None:
        self.DB.insert({"usuario": self.usuario, "sitio": sitio, "status":status, "UID":UID})

# class dbActualizar():
#     def __init__(self) -> None:
#         self.DB = TinyDB("sitiosRefresh.json")

#     def guardarPagina(self, kwargs):
#         self.DB.insert({"nombre": kwargs["nombre"], "url": kwargs["url"], "data":kwargs["data"]})
        