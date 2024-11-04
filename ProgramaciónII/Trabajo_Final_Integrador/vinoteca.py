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
    
    @staticmethod
    def  obtenerBodegas(orden=None, reverso=False):
        for bodega in Vinoteca.obtener_bodegas():
            if isinstance(orden, str):
                if orden == bodega.nombre:
                    print(bodega.id)
    
    @classmethod
    def obtener_cepas(cls):
        return cls.__cepas if cls.__cepas is not None else []
    
    @staticmethod
    def obtenerCepas(orden=None, reverso=False):
        for cepa in Vinoteca.obtener_cepas():
            if isinstance(orden, str):
                if orden == cepa.nombre:
                    print(cepa.id)
    
    @classmethod
    def obtener_vinos(cls):
        return cls.__vinos if cls.__vinos is not None else []
        
    # vinoteca.py
    @staticmethod
        
    def obtenerVinos(orden=None, reverso=False):
         print("====VINOS====")
         for vino in Vinoteca.obtener_vinos():
            if isinstance(orden, str):
             if orden == vino.nombre:
                print(f"Nombre: {vino.nombre}\n Bodega: {vino._Vino__bodega}\n Cepas: {vino._Vino__cepas}\n ID: {vino.id}\n {vino._Vino__partidas}")
            elif vino.obtenerBodega() and orden == vino.obtenerBodega().obtenerNombre():
                print(f"Bodega: {vino._Vino__bodega}\n Nombre: {vino.nombre}\n Cepas: {vino._Vino__cepas}\n ID: {vino.id}")
            elif orden in vino._Vino__cepas:
                print(f"Cepas: {vino._Vino__cepas}\nBodega: {vino._Vino__bodega}\n Nombre: {vino.nombre}\n ID: {vino.id}")
                   
    @staticmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)
        
    @staticmethod
    def buscarBodega(id):
        for bodega in Vinoteca.__bodegas:
         if bodega.obtenerId() == id:
            return bodega
        return None

    @staticmethod
    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

        
    @staticmethod
    def buscarVino(id):
        for vino in Vinoteca.__vinos:
         if vino.obtenerId() == id:
            return vino
        return None

        
    @staticmethod
    def __parsearArchivoDeDatos():
        try:
            with open(Vinoteca.__archivoDeDatos, "r", encoding="utf-8") as archivo: # Paso 1: Abrir el archivo con un bloque 'with'
                datos = json.load(archivo)# Paso 2: Cargar el contenido del archivo como diccionario usando json.load()
                #print("Datos cargados del archivo:", datos)
            return datos  # Retorna el diccionario cargado del archivo JSON
        except FileNotFoundError:
            print(f"El archivo {Vinoteca.__archivoDeDatos} no fue encontrado.")
            return None
        
    @staticmethod
    def __convertirJsonAListas(lista):
        for bodega in lista["bodegas"]:
             Vinoteca.__bodegas.append(Bodega(bodega["id"], 
                                             bodega["nombre"],))

        for vino in lista["vinos"]:
            Vinoteca.__vinos.append(Vino(vino["id"],
                                         vino["nombre"], 
                                         vino["bodega"],
                                         vino["cepas"],
                                         vino["partidas"]))

        for cepa in lista["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"], 
                                         cepa["nombre"]))

v=Vinoteca
v.inicializar()
v.obtenerBodegas("Casa La Primavera Bodegas y Viñedos")
v.obtenerCepas("Malbec")
v.buscarBodega("a0117be3-2ea6-8db1-8901-1be2adf61c29")
v.buscarCepa("e076a2c8-b1f5-136e-8319-0ee0b5c02091")
v.buscarVino("51461f52-89b8-d702-0673-2cc5ac75085c")
 

