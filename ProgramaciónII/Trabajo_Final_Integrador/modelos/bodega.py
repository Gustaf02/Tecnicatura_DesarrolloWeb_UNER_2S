import json
from vinoteca import Vinoteca

class Bodega:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    # Consultas

    """Se recuperan todos los vinos de la vinoteca y se filtran aquellos que pertenecen a la bodega."""
    def obtenerVinos(self):
        todos_vinos = Vinoteca.obtenerVinos()
        vinos_bodega = [vino for vino in todos_vinos if vino.bodega_id == self.id]
        return vinos_bodega
    
    """Se obtienen todos los vinos de la vinoteca y  se filtran de acuerdo con las cepas."""
    def obtenerCepas(self):
        vinos_bodega = self.obtenerVinos()
        cepas_bodega = {vino.cepa for vino in vinos_bodega}
        return list(cepas_bodega)

    def __repr__(self):
        return json.dumps(self.convertirAJSON())
    
    """La bodega representa un diccionario JSON básico."""
    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    """En este caso, se convierte a la bodega en un diccionario JSON completo."""
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
