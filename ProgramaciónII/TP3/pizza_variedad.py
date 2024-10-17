class PizzaVariedad:
    # Constructor que inicializa los atributos 'nombreVariedad' y 'precio'.
    # Si el precio es menor o igual a 0, lanza un error para asegurar validez.
    def __init__(self, nomVar: str, pre: float):
        if pre <= 0:
            raise ValueError("El precio debe ser mayor a 0")  # Validación del precio.
        self.nombreVariedad = nomVar  # Nombre de la variedad de pizza.
        self.precio = pre  # Precio de la variedad.

    # Método para obtener el precio de la variedad.
    def obtener_precio(self):
        return self.precio  # Devuelve el precio actual.

    # Método especial para representar la variedad en formato string.
    # Por ejemplo: "Muzzarella - 500$".
    def __str__(self):
        return f"{self.nombreVariedad} - {self.precio}$"  # Representación textual del objeto.

    # Método para cambiar el nombre de la variedad.
    def establecer_nombre_variedad(self, nom_var: str):
        self.nombreVariedad = nom_var  # Asigna un nuevo nombre a la variedad.

    # Método para establecer un nuevo precio.
    
    def establecer_precio(self, pre: int):
        self.precio = pre  # Actualiza el precio.

    # Método para obtener el nombre de la variedad. 
    
    def obtener_nombre(self):
        return self.nombreVar  

    
