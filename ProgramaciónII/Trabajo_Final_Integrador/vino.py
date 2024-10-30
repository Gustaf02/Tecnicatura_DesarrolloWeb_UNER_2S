from modelos.entidadvineria import EntidadVineria
from modelos.vinoteca import Vinoteca
import json

class Vino(EntidadVineria):
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list[str], partidas: list[int]):
        """
        Constructor de la clase Vino
        Args:
            id (str): Identificador único del vino
            nombre (str): Nombre del vino
            bodega (str): ID de la bodega que produce el vino
            cepas (list[str]): Lista de IDs de las cepas del vino
            partidas (list[int]): Lista de años de las partidas disponibles
        """
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

    # Comandos (setters)
    def establecerBodega(self, bodega: str):
        """Establece el ID de la bodega del vino"""
        self.__bodega = bodega
    
    def establecerCepas(self, cepas: list[str]):
        """Establece la lista de IDs de cepas del vino"""
        self.__cepas = cepas
    
    def establecerPartidas(self, partidas: list[int]):
        """Establece la lista de años de las partidas del vino"""
        self.__partidas = partidas

    # Consultas (getters)
    def obtenerBodega(self):
        """
        Retorna el objeto Bodega asociado al vino
        Returns:
            Bodega: Objeto bodega que produce el vino
        """
        return Vinoteca.buscarBodega(self.__bodega)
    
    def obtenerCepas(self):
        """
        Retorna la lista de objetos Cepa del vino
        Returns:
            list[Cepa]: Lista de objetos Cepa
        """
        return [Vinoteca.buscarCepa(cepa) for cepa in self.__cepas]
    
    def obtenerPartidas(self):
        """
        Retorna la lista de años de las partidas
        Returns:
            list[int]: Lista de años
        """
        return self.__partidas

    def __repr__(self):
        """Representación string del vino"""
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        """
        Convierte el vino a formato JSON básico
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
        Convierte el vino a formato JSON completo
        Returns:
            dict: Diccionario con toda la información del vino
        """
        return self.convertirAJSON()

    def __mapearCepas(self):
        """
        Método auxiliar para convertir las cepas a lista de nombres
        Returns:
            list[str]: Lista con los nombres de las cepas
        """
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
