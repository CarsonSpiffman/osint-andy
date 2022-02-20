from coloresClass import coloramaClass

def utilRespuestas(func: str, dato: str) -> str:
    colores = coloramaClass()
    if func == "guardarPagina":
        return(f"{colores.fondoVerde} {colores.letraNegra} [✓] Pagina {dato} guardada correctamente {colores.resetearColor}")
