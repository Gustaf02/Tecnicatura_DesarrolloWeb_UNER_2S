import json
from modelos.entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    # Consultas: Se recuperan vinos de la vinoteca
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtener_vinos()
        if todos_vinos is not None:
            vinos_cepa = [vino for vino in todos_vinos if self.id in vino.obtenerCepasIds()]
            return vinos_cepa
        return []
    
    def __repr__(self):
        return json.dumps(self.convertirAJSON())

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
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        if isinstance(other, Cepa):
            return self.id == other.id
        return False
