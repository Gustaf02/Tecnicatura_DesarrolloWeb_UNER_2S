from pizza import Pizza

class Maestro_pizzero :
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def establecer_nombre (self, nom):
        self.nom = nom

    def tomar_pedido (self, var):
        var = (input("opcion 1 tomar pedido: "))
        self.piz = Pizza(var)
        self.pizzas_por_cocinar.append(self.piz.var)
        
    def cocinar (self ):
         if len(self.pizzas_por_cocinar)>0:
            orden_pizzas = self.pizzas_por_cocinar[0]
            self.pizzas_por_cocinar.remove(orden_pizzas)
            self.pizzas_por_entregar.append(orden_pizzas)
            #print(f"Pizzas por entregar: {self.pizzas_por_entregar}")
   
    #Gustavo toma los 2 objetos de la lista pizzas_por_entregar y eliminarlos
    def entregar (self):
        if len(self.pizzas_por_entregar) > 0:
            return print(self.pizzas_por_entregar[:2])
        
    def obtener_nombre (self):
        self.nombre = self.nombre
        return print(self.nombre)

    def obtener_pizzas_por_cocinar (self):
        return print(self.pizzas_por_cocinar)
    
    def obtener_pizzas_por_entregar (self):
        return print(self.pizzas_por_entregar)
    








