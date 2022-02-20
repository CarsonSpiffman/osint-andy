from dbClass import dbGuardar
from coloresClass import coloramaClass
import asyncio
import aiohttp
import json
import uuid

class funcionesAsync():
    def __init__(self, usuario: str) -> None:
        self.colores = coloramaClass()
        self.tasks = []
        self.json = "sitiosRefresh.json"
        self.usuario = usuario
        self.UID = str(uuid.uuid4()).split("-")[0]
        self.DB = dbGuardar(self.usuario, self.UID)
    
    def guardarResultados(self, usuario: str, url: str, status: str, UID: str) -> None:
        self.DB.guardarResultados(usuario, url, status, UID)
    
    async def peticionesWebAsync(self, url: str, usuario: str, UID: str) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=15, allow_redirects=False) as response:
                if response.status == 200:
                    self.guardarResultados(usuario, url, response.status, UID)
                    print(f"{self.colores.fondoVerde} {self.colores.letraNegra} [{response.status}] [{url}] -> [{usuario}] [{UID}] {self.colores.resetearColor}")
                else:
                    print(f"{self.colores.fondoRojo} {self.colores.letraNegra} [{response.status}] [{url}] -> [{usuario}] [{UID}] {self.colores.resetearColor}")

                
    async def main(self) -> None:
        with open(self.json, 'r', encoding="utf8") as file:
            data = json.load(file)
            
        for i in range(1, int(len(data["sitiosRecopilados"])+1)):
            task = asyncio.ensure_future(self.peticionesWebAsync(data["sitiosRecopilados"][str(i)]["url"].format(self.usuario), self.usuario, self.UID))
            self.tasks.append(task)

        await asyncio.gather(*self.tasks, return_exceptions=True)
        
    def osint(self) -> None:
        asyncio.get_event_loop().run_until_complete(self.main())
        print(f"{self.colores.fondoCyan} {self.colores.letraNegra} [✓] Datos guardados en {self.usuario}_{self.UID}.json {self.colores.resetearColor}")