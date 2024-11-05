import json


class Vino:
    def __init__(self, id, nombre, bodega, cepas, partida):
        self.id=id
        self.nombre=nombre
        self.bodega=bodega
        self.cepas=cepas
        self.partida=partida

    # def __repr__(self):
    #     return json.dumps({"nombre": self.obtenerNombre()})

    # def convertirAJSON(self):
    #     return {
    #         "id": self.obtenerId(),
    #         "nombre": self.obtenerNombre(),
    #         "bodega": self.obtenerBodega().obtenerNombre(),
    #         "cepas": self.__mapearCepas(),
    #         "partidas": self.__partidas,
    #     }

    # def convertirAJSONFull(self):
    #     return {
    #         "id": self.obtenerId(),
    #         "nombre": self.obtenerNombre(),
    #         "bodega": self.obtenerBodega().obtenerNombre(), 
    #         "cepas": self.__mapearCepas(),
    #         "partidas": self.__partidas,
    #     }

    # def __mapearCepas(self):
    #     cepas = self.obtenerCepas()
    #     cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
    #     return list(cepasMapa)
