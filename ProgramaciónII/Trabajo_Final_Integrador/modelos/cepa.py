import json 
from vinoteca import Vinoteca
from entidadvineria import EntidadVineria

class Cepa:

  def __init__(self, id, nombre): 
    # self.id = id 
    # self.nombre = nombre 

    super().__init__(id, nombre)

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
    
   