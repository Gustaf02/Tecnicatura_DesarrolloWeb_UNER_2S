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
    def obtener_bodegas(cls, orden=None, reverso=False):
        bodegas = cls.__bodegas
        if orden:
            bodegas = sorted(bodegas, key=lambda b: getattr(b, orden), reverse=reverso)
        return bodegas

    @classmethod
    def obtener_cepas(cls, orden=None, reverso=False):
        cepas = cls.__cepas if cls.__cepas is not None else []
        if orden:
            cepas = sorted(cepas, key=lambda c: getattr(c, orden), reverse=reverso)
        return cepas

    @classmethod
   
    def obtener_vinos(cls, orden=None, reverso=False, anios=None):
        vinos = cls.__vinos if cls.__vinos is not None else []
    
        if anios:        
            if isinstance(anios, str):
                anios = [int(anio) for anio in anios.split(',')]
        if anios:
            vinos = [vino for vino in vinos if any(anio in vino.obtenerPartidas() for anio in anios)]
        
        if orden:
            vinos = sorted(vinos, key=lambda v: getattr(v, orden), reverse=reverso)
        return vinos

    @staticmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        if datos is not None:
            Vinoteca.__convertirJsonAListas(datos)
        else:
            print("Error: No se pudieron cargar los datos del archivo JSON.")

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
            with open(Vinoteca.__archivoDeDatos, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except FileNotFoundError:
            print(f"El archivo {Vinoteca.__archivoDeDatos} no fue encontrado.")
            return None
        except json.JSONDecodeError:
            print("Error al cargar los datos de JSON.")
            return None

    @staticmethod
    def __convertirJsonAListas(lista):
        for bodega in lista["bodegas"]:
            Vinoteca.__bodegas.append(Bodega(bodega["id"], bodega["nombre"]))
        for vino in lista["vinos"]:
            Vinoteca.__vinos.append(Vino(vino["id"], vino["nombre"], vino["bodega"], vino["cepas"], vino["partidas"]))
        for cepa in lista["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"], cepa["nombre"]))
