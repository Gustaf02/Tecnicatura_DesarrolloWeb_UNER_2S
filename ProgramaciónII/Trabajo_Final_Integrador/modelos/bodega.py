<<<<<<< HEAD
import json

from modelos.entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        # self.id = id
        # self.nombre = nombre
        # self.cepas = []
        # self.vinos = []

        super().__init__(id, nombre) 
        self.cepas = [] 
        self.vinos = []

    # Consultas: Se recuperan todos los vinos de la vinoteca y se filtran aquellos que pertenecen a la bodega.
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtener_vinos()
        if todos_vinos is not None:
         vinos_bodega = [vino for vino in todos_vinos if vino.obtenerBodega() and vino.obtenerBodega().obtenerId() == self.id]
         self.vinos = vinos_bodega
         return vinos_bodega
        return []


    # Se obtienen todos los vinos de la vinoteca y se filtran de acuerdo con las cepas.
    def obtenerCepas(self):
        vinos_bodega = self.obtenerVinos()
        cepas_bodega = {cepa for vino in vinos_bodega for cepa in vino.obtenerCepas()}
        self.cepas = list(cepas_bodega)
        return list(cepas_bodega)


    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    # La bodega representa un diccionario JSON básico.
    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    # En este caso, se convierte a la bodega en un diccionario JSON completo.
    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    # Métodos privados para mapear cepas y vinos
    def __mapearCepas(self):
     cepas = self.obtenerCepas()
     return [cepa.nombre for cepa in cepas]

    def __mapearVinos(self):
     vinos = self.obtenerVinos()
     return [vino.nombre for vino in vinos]


=======
import json

from modelos.entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        # self.id = id
        # self.nombre = nombre
        # self.cepas = []
        # self.vinos = []

        super().__init__(id, nombre) 
        self.cepas = [] 
        self.vinos = []

    # Consultas: Se recuperan todos los vinos de la vinoteca y se filtran aquellos que pertenecen a la bodega.
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtenerVinos()
        print(f"Todos los vinos: {todos_vinos}")
        if todos_vinos is not None: 
            vinos_bodega = [vino for vino in todos_vinos if vino.obtenerBodega() and vino.obtenerBodega().obtenerId() == self.id]
            self.vinos = vinos_bodega 
            print(f"Vinos de la bodega {self.nombre}: {vinos_bodega}")
            return vinos_bodega 
        return []

    # Se obtienen todos los vinos de la vinoteca y se filtran de acuerdo con las cepas.
    def obtenerCepas(self):
        vinos_bodega = self.obtenerVinos()
        print(f"Vinos de la bodega {self.nombre} para obtener cepas: {vinos_bodega}")
        cepas_bodega = {cepa.obtenerId() for vino in vinos_bodega for cepa in vino.obtenerCepas()}
        self.cepas = list(cepas_bodega)
        print(f"Cepas de la bodega {self.nombre}: {cepas_bodega}")
        return list(cepas_bodega)

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    # La bodega representa un diccionario JSON básico.
    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    # En este caso, se convierte a la bodega en un diccionario JSON completo.
    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    # Métodos privados para mapear cepas y vinos
    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.nombre, cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.nombre, vinos)
        return list(vinosMapa)

>>>>>>> f8e458ad459d2982b68be198fa930f6102e3afcb
    