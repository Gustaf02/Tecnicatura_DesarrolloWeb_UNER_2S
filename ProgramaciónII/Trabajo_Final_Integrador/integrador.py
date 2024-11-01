# librerias
import os
import json
from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def establecerNombre(self, nombre):
        self.nombre = nombre
    
    def obtenerId(self):
        return self.id
    
    def obtenerNombre(self):
        return self.nombre
    
    def __eq__(self, orden:None):
        return isinstance(orden, EntidadVineria) and self.id == orden.id

    @abstractmethod
    def convertirAJSON(self):
        pass


class Vino():
    # Inicializador de vino con sus atributos
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partida: list):
        """
        Constructor de la clase Vino
        Args:
            id (str): Identificador único del vino
            nombre (str): Nombre del vino
            bodega (str): ID de la bodega que produce el vino
            cepas (list): Lista de IDs de las cepas del vino
            partidas (list): Lista de años de las partidas disponibles
        """
        #super().__init__(id, nombre)
        self.id = id
        self.nombre = nombre
        self.bodega = bodega
        self.cepas = cepas
        self.partida = partida

    # Comandos (setters)
    def establecerBodega(self, bodega: str):
        """Establece el ID de la bodega del vino"""
        self.__bodega = bodega

    def establecerCepas(self, cepas: list):
        """Establece la lista de IDs de cepas del vino"""
        self.__cepas = cepas

    def establecerPartidas(self, partidas: list):
        """Establece la lista de años de las partidas del vino"""
        self.__partidas = partidas

    # Consultas (getters)
    def obtenerBodega(self):
        """
        Retorna el objeto Bodega asociado al vino
        Returns:
            Bodega: objeto Bodega que produce el vino
        """
        return Vinoteca.buscarBodega(self.__bodega)

    def obtenerCepas(self):
        """
        Retorna la lista de objetos Cepa asociados al vino
        Returns:
            list: Lista de objetos Cepa
        """
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self.__cepas if Vinoteca.buscarCepa(cepa_id)]

    def obtenerPartidas(self):
        """
        Retorna la lista de años de las partidas
        Returns:
            list: Lista de años (int)
        """
        return self.__partidas

    # Métodos de representación
    def __repr__(self):
        """Representación en string del vino"""
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        """
        Convierte el vino a formato JSON para listados
        Returns:
            dict: Diccionario con la información básica del vino
        """
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.obtenerPartidas()
        }

    def convertirAJSONFull(self):
        """
        Convierte el vino a formato JSON para vista detallada
        Returns:
            dict: Diccionario con toda la información del vino
        """
        return self.convertirAJSON()

    # Conversión de cepas a nombres
    def __mapearCepas(self):
        """
        Convierte la lista de objetos Cepa a lista de nombres
        Returns:
            list: Lista de nombres de cepas
        """
        cepas = self.obtenerCepas()
        return [cepa.obtenerNombre() for cepa in cepas]

    # Métodos de verificación
    def tienePartida(self, anio):
        """
        Verifica si el vino tiene una partida de un año específico
        Args:
            anio (int): Año a buscar
        Returns:
            bool: True si tiene partida del año especificado, False en caso contrario
        """
        return anio in self.obtenerPartidas()


class Cepa():

  def __init__(self, id, nombre): 
    self.id = id 
    self.nombre = nombre 

    #super().__init__(id, nombre)

    # Consultas: Se recuperan vinos de la vinoteca
    def obtenerVinos(self): 
         todos_vinos = Vinoteca.obtenerVinos() 
         vinos_cepa = [vino for vino in todos_vinos if vino.cepa_id == self.id] 
         return vinos_cepa
        
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    # Métodos privados. Se mapean vinos. 
    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
    
   

class Bodega:
    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre

    # def __repr__(self):
    #     return json.dumps(self.convertirAJSON())

    # def convertirAJSON(self):
    #     return {
    #         "id": self.obtenerId(),
    #         "nombre": self.obtenerNombre(),
    #         "cepas": self.__mapearCepas(),
    #         "vinos": len(self.obtenerVinos()),
    #     }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    # def __mapearCepas(self):
    #     cepas = self.obtenerCepas()
    #     cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
    #     return list(cepasMapa)

    # def __mapearVinos(self):
    #     vinos = self.obtenerVinos()
    #     vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
    #     return list(vinosMapa)




class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []
    @classmethod

    def obtener_bodegas(cls):
        return cls.__bodegas
    def  obtenerBodegas(orden=None, reverso=False):
        for bodega in Vinoteca.obtener_bodegas():
            if isinstance(orden, str):
                if orden == bodega.nombre:
                    print(bodega.id)
    
    @classmethod
    def obtener_cepas(cls):
        return cls.__cepas
    def obtenerCepas(orden=None, reverso=False):
        for cepa in Vinoteca.obtener_cepas():
            if isinstance(orden, str):
                if orden == cepa.nombre:
                    print(cepa.id)
    
    @classmethod
    def obtener_vinos(cls):
        return cls.__vinos
    def obtenerVinos(orden=None, reverso=False):
        print("====VINOS====")
        for vino in Vinoteca.obtener_vinos():
             if isinstance(orden, str):
                if orden == vino.nombre:
                    print(f"Nombre: {vino.nombre}\n Bodega: {vino.bodega}\n Cepas: {vino.cepas}\n ID: {vino.id}\n {vino.partida}")
                elif orden == vino.bodega:
                    print(f"Bodega: {vino.bodega}\n Nombre: {vino.nombre}\n Cepas: {vino.cepas}\n ID: {vino.id}")
                elif orden == vino.cepas:
                    print(f"Cepas: {vino.cepas}\nBodega: {vino.bodega}\n, Nombre: {vino.nombre}\n,ID: {vino.id}")
                     
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)
        
    def buscarBodega(id):
        for bodega in Vinoteca.obtener_bodegas():
            if isinstance(id, str):
                if id == bodega.id:
                    print(bodega.nombre)
        

    def buscarCepa(id):
        for cepa in Vinoteca.obtener_cepas():
            if isinstance(id, str):
                if id == cepa.id:
                    print(cepa.nombre)
        

    def buscarVino(id):
        for vino in Vinoteca.obtener_vinos():
            if isinstance(id, str):
                if id == vino.id:
                    print(vino.nombre)
        

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
                                         vino["cepas"],
                                         vino["partidas"]))

        for cepa in lista["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"], 
                                         cepa["nombre"]))


"""
Instancias vinoteca pruebas
"""            
v=Vinoteca
v.inicializar()
v.obtenerBodegas("Casa La Primavera Bodegas y Viñedos")
v.obtenerCepas("Malbec")
v.obtenerVinos("Escandalosos")
v.buscarBodega("a0117be3-2ea6-8db1-8901-1be2adf61c29")
v.buscarCepa("e076a2c8-b1f5-136e-8319-0ee0b5c02091")
v.buscarVino("51461f52-89b8-d702-0673-2cc5ac75085c")

"""
Instancias vino prueba
"""

            

