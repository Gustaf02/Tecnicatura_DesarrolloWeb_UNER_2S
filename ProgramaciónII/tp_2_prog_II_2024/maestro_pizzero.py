from pizza import Pizza
#from mozo import Mozo

class Maestro_pizzero :
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def establecer_nombre (self, nom):
        self.nom = nom

    def tomar_pedido (self, var):
        var = (input("opcion 1 tomar pedido: "))
        self.piza_de = Pizza(var)
        self.pizzas_por_cocinar.append(self.piza_de.var)
        print(f"Objeto creado por pizzero: {self.piza_de}")
        
    def cocinar (self ):
         if len(self.pizzas_por_cocinar)>0:
            orden_pizzas = self.pizzas_por_cocinar[0]
            self.pizzas_por_cocinar.remove(orden_pizzas)
            self.pizzas_por_entregar.append(orden_pizzas)
            #print(f"Pizzas por entregar: {self.pizzas_por_entregar}")
   
    #Gustavo toma los 2 objetos de la lista pizzas_por_entregar y eliminarlos
    def entregar (self):
        return print(self.pizzas_por_entregar[:2]) #and self.#pizzas_por_entregar.pop(1))
        
    def obtener_nombre (self):
        self.nombre = self.nombre
        return print(self.nombre)

    def obtener_pizzas_por_cocinar (self):
        return print(self.pizzas_por_cocinar)
    
    def obtener_pizzas_por_entregar (self):
        #retira = Mozo.tomar_pizzas(self, self.pizzas_por_entregar[:2])
        #self.pizzas_por_entregar.remove(retira)     

        return print(self.pizzas_por_entregar)
    








