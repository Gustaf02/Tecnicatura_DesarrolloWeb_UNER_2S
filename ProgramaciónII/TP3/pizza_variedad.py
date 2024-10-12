class Pizza_variedad :
    def __init__(self, nom_var, pre : float):
        self.nombre_var = nom_var
        self.pre = pre
        self.set = []

    def crear_variedad(self, nom_var, pre):

        refe_obj = input("Cree un articulo: ")
        nom_var = input("Ingrese un nombre: ")
        pre = float(input("Ingrese el precio: "))
        refe_obj = Pizza_variedad(nom_var, pre)
        self.set.append(refe_obj.nombre_var)
        self.set.append(refe_obj.nombre_var)
        self.set.append(refe_obj.pre)
        #print(self.set)


    def obtener_set(self):
        print(self.set)
        return  self.set


    
    def establecer_nombre_variedad (self, nom_var : str):
        self.nombre_var = nom_var
    
    def establecer_precio (self, pre : int):
        self.pre = pre
    
    def obtener_nombre (self):
        return self.nombre_var
    
    def obtener_precio (self):
        return self.pre