# Genere la clase MaestroPizzero, conteniendo los atributos y servicios mencionados en
# el diagrama de clases anterior.
# i. El comando tomarPedido debe crear un nuevo objeto de la clase Pizza,
# de la variedad indicada en el parámetro formal var. Una vez inicializado
# dicho objeto, debe este agregarse a la lista referenciada por el atributo
# pizzasPorCocinar.
# ii. El comando cocinar debe tomar todos los objetos de la clase Pizza de la
# lista pizzasPorCocinar y depositarlos en una segunda lista,
# pizzasPorEntregar. Si no hay pizzas por ser cocinadas, el comando no
# tiene efecto sobre el estado interno del objeto.
# iii. El comando entregar retorna hasta un máximo de 2 objetos de la clase
# Pizza de la lista pizzasPorEntregar, removiéndolos de ella. Si no hay
# pizzas para ser entregadas, se debe retornar una lista vacía.

from pizza import Pizza 

# Se inicializan el nombre del maestro pizzero y dos listas donde se van a almacenar  las pizzas aún no cocinadas 
class Maestro_pizzero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

# Se establece el nombre del maestro pizzero
    def establecer_nombre (self, nom):
        self.nom = nom

# Se toma el pedido del cliente y se ingresa la variedad de pizza
    def tomar_pedido(self):
        variedad = input("Ingrese la variedad de pizza: ")  
        pizza = Pizza(variedad)  
        self.pizzas_por_cocinar.append(pizza)
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

# Cocina la primera pizza en la lista de pizzas por cocinar
    def cocinar(self):
        if self.pizzas_por_cocinar:
            pizza_cocinada = self.pizzas_por_cocinar.pop(0)
            self.pizzas_por_entregar.append(pizza_cocinada)
            print(f"Se ha cocinado: {pizza_cocinada.obtener_variedad()}")
            
# Se obtiene el nombre del maestro pizzero
    def obtener_nombre (self):
        self.nombre = self.nombre
        return print(self.nombre)   

# Se muestran las pizzas que aún no han sido cocinadas
    def obtener_pizzas_por_cocinar(self):
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

# Se muestran las pizzas que ya han sido cocinadas y están listas para ser servidas
    def obtener_pizzas_por_entregar(self):
        print(f"Pizzas por entregar: {[p.obtener_variedad() for p in self.pizzas_por_entregar]}")