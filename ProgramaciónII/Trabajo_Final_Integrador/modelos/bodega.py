import json


class Bodega:
    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        c_js = {}
        from vinoteca import Vinoteca
        for c_js in Vinoteca.__bodegas(c_js):
            
            return {
            "id": Vinoteca.obtenerId(),
            "nombre": Vinoteca.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(Vinoteca.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        from vinoteca import Vinoteca   
        for b in Vinoteca.__bodegas:
            return {
            "id": Vinoteca.obtenerId(),
            "nombre": Vinoteca.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
            }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)
