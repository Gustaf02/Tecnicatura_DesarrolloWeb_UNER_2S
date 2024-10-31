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
    @classmethod

    def obtener_bodegas(cls):
        return cls.__bodegas
    def  obtenerBodegas():
        for bodega in Vinoteca.obtener_bodegas():
            pass#print(f"ID: {bodega.id}, Nombre: {bodega.nombre}")
    
    @classmethod
    def obtener_cepas(cls):
        return cls.__cepas
    def obtenerCepas(orden=None, reverso=False):
        for cepa in Vinoteca.obtener_cepas():
            pass#print(f"ID: {cepa.id}, Nombre: {cepa.nombre}")
    
    @classmethod
    def obtener_vinos(cls):
        return cls.__vinos
    def obtenerVinos(orden=None, reverso=False):
        print("====VINOS====")
        for vino in Vinoteca.obtener_vinos():
             if isinstance(orden, str):
                if orden == vino.nombre:
                    print(f"Nombre: {vino.nombre}\n, Bodega: {vino.bodega}\n, Cepas: {vino.cepas}\n,ID: {vino.id}")
                elif orden == vino.bodega:
                    print(f"Bodega: {vino.bodega}\n, Nombre: {vino.nombre}\n, Cepas: {vino.cepas}\n,ID: {vino.id}")
                elif orden == vino.cepas:
                    print(f"Cepas: {vino.cepas}\nBodega: {vino.bodega}\n, Nombre: {vino.nombre}\n,ID: {vino.id}")
                     
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)
        

    # def obtenerBodegas(orden=None, reverso=False):
    #     b=[]
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #            b.append(Vinoteca.obtener_bodegas().sort(key=lambda bodega: bodega.nombre, reverse=False))
    #         elif orden == "vinos":
    #             Vinoteca.__bodegas.sort(key=lambda bodega: len(bodega.vinos), reverse=reverso)
    #     print(b)
    #     return 
    
    
    
        
    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     if isinstance(anio, int):
    #         pass  # completar
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             pass  # completar
    #         elif orden == "bodega":
    #             pass  # completar
    #         elif orden == "cepas":
    #             pass  # completar
    #     pass  # completar

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
        for bodega in lista["bodegas"]:
             Vinoteca.__bodegas.append(Bodega(bodega["id"], 
                                             bodega["nombre"],))

        for vino in lista["vinos"]:
            Vinoteca.__vinos.append(Vino(vino["id"],
                                         vino["nombre"], 
                                         vino["bodega"],
                                         vino["cepas"]))

        for cepa in lista["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"], 
                                         cepa["nombre"]))

v=Vinoteca
v.inicializar()
v.obtenerBodegas()
v.obtenerCepas()
v.obtenerVinos("aa6af203-2f63-4fa8-40ff-3f77af062df8")


