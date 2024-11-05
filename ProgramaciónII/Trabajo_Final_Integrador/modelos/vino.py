import json
from modelos.entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

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
        return self.__partidas

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
