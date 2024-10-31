from modelos.entidadvineria import EntidadVineria
from vinoteca import Vinoteca
import json

class Vino(EntidadVineria):
    # Inicializador de vino con sus atributos
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        """
        Constructor de la clase Vino
        Args:
            id (str): Identificador único del vino
            nombre (str): Nombre del vino
            bodega (str): ID de la bodega que produce el vino
            cepas (list): Lista de IDs de las cepas del vino
            partidas (list): Lista de años de las partidas disponibles
        """
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

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
