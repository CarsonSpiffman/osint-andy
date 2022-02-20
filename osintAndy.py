from asyncClass import funcionesAsync
from utils import utilRespuestas

class osintRecon:
    def __init__(self, usuario: str) -> None:
        self.usuario = usuario
        self.asyncFunciones =  funcionesAsync(self.usuario)
        
    def osint(self):
        self.asyncFunciones.osint()

# class osintDB:
#     def __init__(self) -> None:
#         self.DB = dbActualizar()
    
#     def agregarSitio(self, **kwargs):
#         self.DB.guardarPagina(kwargs)
#         print(utilRespuestas("guardarPagina", kwargs["url"]))