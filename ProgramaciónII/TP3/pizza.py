class Pizza:

    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: str):
        self.__variedad = var

    def establecer_variedad(self, var: str):
        self.__variedad = var

    def establecer_estado_interno (self, estado: int):
        self.estado = estado

    def obtener_variedad(self):
        return self.__variedad
    
    def  ontener_estado_interno (self):
        return self.estado
    def __repr__(self):
        return self.__variedad