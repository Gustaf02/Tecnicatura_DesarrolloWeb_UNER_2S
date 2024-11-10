import json
from modelos.entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas if cepas is not None else []
        self.__partidas = partidas if partidas is not None else []

    # Consultas
    def obtenerBodega(self):
        from vinoteca import Vinoteca
        bodega = Vinoteca.buscarBodega(self.__bodega)
        if bodega is not None:
            return bodega
        return None

    def obtenerCepas(self):
        from vinoteca import Vinoteca
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self.__cepas if Vinoteca.buscarCepa(cepa_id)]
    
    def obtenerCepasIds(self): 
        return self.__cepas

    def obtenerPartidas(self):
        return self.__partidas if self.__partidas else []

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre() if self.obtenerBodega() else None,
            "cepas": self.__mapearCepas(),
            "partidas": self.obtenerPartidas()
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        return [cepa.obtenerNombre() for cepa in cepas]

    def tienePartida(self, anio):
        return anio in self.obtenerPartidas()

    # Comandos (setters)
    def establecerBodega(self, bodega: str):
        """Establece el ID de la bodega del vino"""
        self.__bodega = bodega

    def establecerCepas(self, cepas: list):
        """Establece la lista de IDs de cepas del vino"""
        self.__cepas = cepas if cepas is not None else []

    def establecerPartidas(self, partidas: list):
        """Establece la lista de años de las partidas del vino"""
        self.__partidas = partidas if partidas is not None else []
