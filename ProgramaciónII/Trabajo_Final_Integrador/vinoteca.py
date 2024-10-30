# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)
        

    def obtenerBodegas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                return Vinoteca.__bodegas["nombre"]
        #     elif orden == "vinos":
        #         pass  # completar
        # pass  # completar

    def obtenerCepas(orden=None, reverso=False):
        c=[]
        if isinstance(orden, str):
            if orden == "nombre":
                for n in Vinoteca.__cepas:
                    
                    c.append(n)
                print(c)
                return c
        

        

    def obtenerVinos(anio=None, orden=None, reverso=False):
        if isinstance(anio, int):
            pass  # completar
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        pass  # completar

    def buscarBodega(id):
        pass  # completar

    def buscarCepa(id):
        pass  # completar

    def buscarVino(id):
        pass  # completar

    def __parsearArchivoDeDatos():
        try:
            with open(Vinoteca.__archivoDeDatos, "r", encoding="utf-8") as archivo: # Paso 1: Abrir el archivo con un bloque 'with'
                datos = json.load(archivo)# Paso 2: Cargar el contenido del archivo como diccionario usando json.load()
                #print("Datos cargados del archivo:", datos)
            return datos  # Retorna el diccionario cargado del archivo JSON
        except FileNotFoundError:
            print(f"El archivo {Vinoteca.__archivoDeDatos} no fue encontrado.")
            return None

    def __convertirJsonAListas(lista):
        #print(lista)
        #Carga los datos de las lista bodegas a __bodegas
        contador = 1
        for bodega in lista["bodegas"]:
            
            Vinoteca.__bodegas.append(Bodega(bodega["id"], 
                                             bodega["nombre"],))
            #return Vinoteca.__bodegas
            #Vinoteca.__bodegas.append(bodega)
            # print(f"===BODEGA==={contador}")J
            # print(bodega)
            # contador += 1

        contador = 1    
        for vino in lista["vinos"]:
            Vinoteca.__vinos.append(Vino(vino["id"],
                                         vino["nombre"], 
                                         vino["bodega"],
                                         vino["cepas"]))
            #print(Vinoteca.__vinos)
            # print(f"===VINO==={contador}")
            # print(vino["nombre"])
            # contador += 1

        contador = 1
        for cepa in lista["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"], 
                                         cepa["nombre"]))

            # print(f"===CEPA==={contador}")
            # print(cepa)
            # contador += 1
    
        
    


v=Vinoteca
v.inicializar()
v.obtenerBodegas()
v.obtenerCepas("nombre")

