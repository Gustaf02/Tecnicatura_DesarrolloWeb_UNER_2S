from maestropizzero import MaestroPizzero
from mozo import Mozo
from orden import Orden
from pizzavariedad import PizzaVariedad
from pizza import Pizza

class TesterPizzeria:

    def main(self):
        # Creación de variedades de pizza
        variedades = {
            "1": PizzaVariedad("Muzzarella", 7000.00),
            "2": PizzaVariedad("Fugazetta", 7500.00),
            "3": PizzaVariedad("Napolitana", 7500.00),
            "4": PizzaVariedad("Rúcula y Crudo", 9000.00),
            "5": PizzaVariedad("Calabresa", 8200.00),
            "6": PizzaVariedad("Provolone", 8400.00),
            "7": PizzaVariedad("Roquefort y Nuez", 9000.00)
        }

        ordenes = []  # Lista para almacenar las órdenes
        orden_numero = 1  # Contador de órdenes

        print('----------------------------------------\nPizzería de Don Pipo\n----------------------------------------')

        # Toma de pedidos por parte del usuario
        while True:
            pizzas = []  # Lista de pizzas para cada orden
            print("\nSeleccione las pizzas para la nueva orden:")
            for key, var in variedades.items():
                print(f"{key}: {var.obtenerNombreVariedad()} - Precio: ${var.obtenerPrecio():.2f}")

            print("0: Finalizar la orden")

            while True:
                seleccion = input("Ingrese el número de la pizza que desea agregar (0 para terminar): ")

                if seleccion == "0":
                    if pizzas:
                        ordenes.append(Orden(orden_numero, pizzas))
                        print(f"Orden #{orden_numero} creada con {len(pizzas)} pizzas.")
                        orden_numero += 1
                    break  # Finaliza la toma de pizzas para esta orden
                elif seleccion in variedades:
                    pizza = Pizza(variedades[seleccion])  # Crear objeto Pizza
                    pizzas.append(pizza)
                    print(f"Pizza {variedades[seleccion].obtenerNombreVariedad()} agregada.")
                else:
                    print("Selección no válida. Intente de nuevo.")

            continuar = input("¿Desea crear otra orden? (s/n): ").lower()
            if continuar != 's':
                break

        # Instancias. Creación del maestro pizzero y los mozos
        pipo = MaestroPizzero("Pipo")
        nico = Mozo("Nico")
        juan = Mozo("Juan")

        # Procesar las órdenes creadas
        for orden in ordenes:
            print(f"Pipo tomando pedido #{orden.obtenerNroOrden()}")
            pipo.tomarPedido(orden)

        self.__imprimirEstado(pipo, nico, juan)

        # Cocinar los pedidos
        print("\nCocinando los pedidos...")
        pipo.cocinar()
        self.__imprimirEstado(pipo, nico, juan)

        # Entrega de pizzas por los mozos
        for orden in ordenes:
            self.__procesarEntrega(nico, pipo, orden)  # Nico entrega primero
            self.__procesarEntrega(juan, pipo, orden)  # Luego Juan entrega

        self.__imprimirEstado(pipo, nico, juan)

        # Calcular y mostrar el costo total de las órdenes
        self.__calcularCostoTotal(ordenes)

    def __procesarEntrega(self, mozo: Mozo, maestro: MaestroPizzero, orden: Orden):
        """Método auxiliar para gestionar la entrega y servicio de pizzas."""
        print(f"\n{mozo.obtenerNombre()} entregando pizzas de la orden #{orden.obtenerNroOrden()}")
        pizzas_a_entregar = [p for p in orden.obtenerPizzas() if p.obtenerEstado() == Pizza.ESTADO_COCINADA]
        
        if not pizzas_a_entregar:
            print(f"No hay pizzas cocinadas para entregar de la orden #{orden.obtenerNroOrden()}.")
            return
        
        # Toma hasta 2 pizzas
        pizzas_para_entregar = pizzas_a_entregar[:2]
        mozo.tomarPizzas(pizzas_para_entregar)  

        if mozo.obtenerPizzas():
            mozo.servirPizzas()
            print(f"{mozo.obtenerNombre()} ha entregado {len(mozo.obtenerPizzas())} pizzas de la orden #{orden.obtenerNroOrden()}.")
        else:
            print(f"No hay pizzas para entregar de la orden #{orden.obtenerNroOrden()}.")

    def __imprimirEstado(self, maestro: MaestroPizzero, nico: Mozo, juan: Mozo):
        """Se imprime el estado actual de la pizzería."""
        print("\nEstado actual:")
        print(f"Maestro pizzero: {maestro.obtenerNombre()}")
        print(f"Número de órdenes: {len(maestro.obtenerOrdenes())}")

        print("\nÓrdenes:")
        for orden in maestro.obtenerOrdenes():
            print(f"Orden #{orden.obtenerNroOrden()} - Estado: {orden.obtenerEstadoOrden()} - Pizzas: {[pizza.obtenerVariedad().obtenerNombreVariedad() for pizza in orden.obtenerPizzas()]}")

        print(f"\nMozo {nico.obtenerNombre()} lleva {len(nico.obtenerPizzas())} pizzas.")
        print(f"Mozo {juan.obtenerNombre()} lleva {len(juan.obtenerPizzas())} pizzas.")

    def __calcularCostoTotal(self, ordenes):
        """Se calcula y se muestra el costo total de las órdenes."""
        total = sum(orden.calcularTotal() for orden in ordenes)
        print(f"\nEl costo total de las órdenes es: ${total:.2f}")

# Punto de entrada del programa
if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()

