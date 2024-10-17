from mozo import Mozo
from pizza_variedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestro_pizzero import MaestroPizzero
class Tester:

    @staticmethod
    def pedir_variedad_pizza():
        nombre = input("Ingrese el nombre de la variedad de pizza: ")
        while True:
            try:
                precio = float(input("Ingrese el precio de la pizza: "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
        return PizzaVariedad(nombre, precio)
    @staticmethod
    def pedir_pizzas(variedades):
        pizzas = []
        while True:
            print("Elija una variedad de pizza para agregar a la orden:")
            for i, variedad in enumerate(variedades, 1):
                print(f"{i}. {variedad.nombreVariedad} - {variedad.precio}$")
            
            try:
                eleccion = int(input("Seleccione el número de la variedad (o 0 para terminar): "))
                if eleccion == 0:
                    break
                if 1 <= eleccion <= len(variedades):
                    pizzas.append(Pizza(variedades[eleccion - 1]))
                    print(f"Pizza de {variedades[eleccion - 1].nombreVariedad} agregada.")
                else:
                    print("Opción inválida, intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        return pizzas
    
    @staticmethod
    def crear_orden(nro, variedades):
        pizzas = Tester.pedir_pizzas(variedades)
        return Orden(nro, pizzas)

    @staticmethod
    def mostrar_ordenes(ordenes):
        if not ordenes:
            print("No hay órdenes creadas.")
        else:
            for orden in ordenes:
                estado = {
                    Orden.ESTADO_INICIAL: "Inicial",
                    Orden.ESTADO_PARA_ENTREGAR: "Para Entregar",
                    Orden.ESTADO_ENTREGADA: "Entregada"
                }[orden.estadoOrden]
                print(f"Orden N° {orden.nroOrden} - Estado: {estado}")
                for pizza in orden.pizzas:
                    estado_pizza = {
                        Pizza.ESTADO_POR_COCINAR: "Por Cocinar",
                        Pizza.ESTADO_COCINADA: "Cocinada",
                        Pizza.ESTADO_ENTREGADA: "Entregada"
                    }[pizza.estado]
                    print(f"   Pizza: {pizza.variedad.nombreVariedad} - Estado: {estado_pizza}")

    @staticmethod
    def main():
        maestro = MaestroPizzero("Pipo")
        mozo = Mozo("Nico")
        mozo2 = Mozo("Juan")
        variedades = []
        ordenes = []
        nro_orden = 1

        while True:
            print("\n=== Menú ===")
            print("1. Crear variedad de pizza")
            print("2. Crear orden")
            print("3. Agregar pizzas a una orden")
            print("4. Ver órdenes")
            print("5. Pizzero tomar pedido")
            print("6. Pizzero cocinar pizzas")
            print("7. Mozo 1 servir pizza")
            print("8. Mozo 2 servir pizza")
            print("9. Ver estado del mozos")
            print("10. obtener cuanta")
            print("11. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Crear variedad de pizza
                variedad = Tester.pedir_variedad_pizza()
                variedades.append(variedad)
                print(f"Variedad {variedad.nombreVariedad} creada con éxito.")

            elif opcion == "2":
                # Crear orden
                if variedades:
                    orden = Tester.crear_orden(nro_orden, variedades)
                    if orden.pizzas:
                        maestro.tomarPedido(orden)
                        ordenes.append(orden)
                        print(f"Orden {nro_orden} creada y agregada al maestro pizzero.")
                        nro_orden += 1
                    else:
                        print("La orden no tiene pizzas, no se agregó.")
                else:
                    print("Debe crear variedades de pizza antes de generar una orden.")

            elif opcion == "3":
                # Agregar pizzas a una orden existente
                if ordenes:
                    Tester.mostrar_ordenes(ordenes)
                    try:
                        nro = int(input("Ingrese el número de la orden a la que desea agregar pizzas: "))
                        orden = next((o for o in ordenes if o.nroOrden == nro), None)
                        if orden:
                            nuevas_pizzas = Tester.pedir_pizzas(variedades)
                            orden.pizzas.extend(nuevas_pizzas)
                            print(f"Pizzas agregadas a la orden {nro}.")
                        else:
                            print("No se encontró una orden con ese número.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                else:
                    print("No hay órdenes creadas.")

            elif opcion == "4":
                # Ver órdenes
                Tester.mostrar_ordenes(ordenes)

            elif opcion == "5":
                # Pizzero toma pedido
                if ordenes:
                    for orden in ordenes:
                        if orden.estadoOrden == Orden.ESTADO_INICIAL:
                            maestro.tomarPedido(orden)
                    print("El maestro pizzero ha tomado todos los pedidos pendientes.")
                else:
                    print("No hay órdenes disponibles para tomar.")
            elif opcion == "6":
                # Pizzero cocina pizzas
                if ordenes:
                    maestro.cocinar()
                else:
                    print("No hay órdenes para cocinar.")

            elif opcion == "7":
                # Mozo servir pizzas
                if ordenes:
                    Tester.mostrar_ordenes(ordenes)
                    try:
                        nro = int(input("Ingrese el número de la orden de la cual desea servir pizzas: "))
                        orden = next((o for o in ordenes if o.nroOrden == nro), None)
                        if orden:
                            pizzas_servir = maestro.entregar(orden)
                            if pizzas_servir:
                                mozo.tomarPizzas(pizzas_servir)
                                mozo.servirPizzas()
                            else:
                                print(f"No hay pizzas listas para entregar en la orden N° {nro}.")
                        else:
                            print("No se encontró una orden con ese número.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                else:
                    print("No hay órdenes creadas.")

            elif opcion == "8":
                # Mozo servir pizzas
                if ordenes:
                    Tester.mostrar_ordenes(ordenes)
                    try:
                        nro = int(input("Ingrese el número de la orden de la cual desea servir pizzas: "))
                        orden = next((o for o in ordenes if o.nroOrden == nro), None)
                        if orden:
                            pizzas_servir = maestro.entregar(orden)
                            if pizzas_servir:
                                mozo2.tomarPizzas(pizzas_servir)
                                mozo2.servirPizzas()
                            else:
                                print(f"No hay pizzas listas para entregar en la orden N° {nro}.")
                        else:
                            print("No se encontró una orden con ese número.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                else:
                    print("No hay órdenes creadas.")

            elif opcion == "9":
                # Ver estado del mozo
                if mozo.obtenerEstadoLibre():
                    print(f"El mozo {mozo.obtenerNombre()} está libre.")
                else:
                    print(f"El mozo {mozo.obtenerNombre()} está sirviendo pizzas.")
                    pizzas_mozo = mozo.obtenerPizzas()
                    for pizza in pizzas_mozo:
                        print(f"   Pizza: {pizza.variedad.nombreVariedad} - Estado: {pizza.estado}")
                if mozo.obtenerEstadoLibre():
                    print(f"El mozo {mozo2.obtenerNombre()} está libre.")
                else:
                    print(f"El mozo {mozo2.obtenerNombre()} está sirviendo pizzas.")
                    pizzas_mozo = mozo2.obtenerPizzas()
                    for pizza in pizzas_mozo:
                        print(f"   Pizza: {pizza.variedad.nombreVariedad} - Estado: {pizza.estado}")
                
            elif opcion == "10":
                # Mostrar el total de la cuenta de una orden
                if ordenes:
                    Tester.mostrar_ordenes(ordenes)
                    try:
                        nro = int(input("Ingrese el número de la orden para ver el total: "))
                        orden = next((o for o in ordenes if o.nroOrden == nro), None)
                        if orden:
                            total = sum(pizza.variedad.precio for pizza in orden.pizzas)
                            print(f"El total de la orden N° {nro} es: {total:.2f}$")
                        else:
                            print("No se encontró una orden con ese número.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                else:
                    print("No hay órdenes creadas.")


            elif opcion == "11":
                # Salir del programa
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida, por favor seleccione una opción del 1 al 10.")
               
# Bloque final para ejecutar el tester
if __name__ == "__main__":
    tester = Tester
    tester.main()

            
            

        

        #AGREGO PIZZAS A LA LISTA self.pizza DE Ordenes
        #   orden 1
        # orden_1.pizzas.append(pizza_1.obtener_variedad().obtener_nombre())
        # orden_1.pizzas.append(pizza_1.ESTADO_POR_COCINAR)
        # orden_1.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_1.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        # orden_1.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        # orden_1.pizzas.append(pizza_3.ESTADO_POR_COCINAR)

        # #   orden 2
        # orden_2.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        # orden_2.pizzas.append(pizza_3.ESTADO_POR_COCINAR)
        # orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_2.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        # orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_2.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        # orden_2.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        # orden_2.pizzas.append(pizza_3.ESTADO_POR_COCINAR)
        # orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_2.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        
        # #   orden 3
        # orden_3.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        # orden_3.pizzas.append(pizza_3.ESTADO_POR_COCINAR)
        # orden_3.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_3.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        # orden_3.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_3.pizzas.append(pizza_2.ESTADO_POR_COCINAR)

        # #   orden 4
        # orden_4.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        # orden_4.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        # orden_4.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())

        # print("--------------------------------------------------------------------") 
        # print(f"Nro de orden {orden_1.num_orden}, estado {orden_1.ESTADO_INICIAL}")
        # print(orden_1.obtener_pizzas())
        # print("--------------------------------------------------------------------")
        # print(f"Nro de orden {orden_4.num_orden}, estado {orden_4.ESTADO_INICIAL}")
        # print(orden_2.obtener_pizzas())
        # print("--------------------------------------------------------------------")
        # print(f"Nro de orden {orden_3.num_orden}, estado {orden_3.ESTADO_INICIAL}")
        # print(orden_3.obtener_pizzas())
        # print("--------------------------------------------------------------------")
    
        #CLASE Maestro_pizzero 
        # pizzero.tomar_pedido(orden_1.num_orden)
        # pizzero.tomar_pedido(orden_1.ESTADO_INICIAL)
        # pizzero.tomar_pedido(orden_1.pizzas)
       
        
        # pizzero.tomar_pedido(orden_2.num_orden)
        # pizzero.tomar_pedido(orden_2.ESTADO_INICIAL)
        # pizzero.tomar_pedido(orden_2.pizzas)
        

        # pizzero.tomar_pedido(orden_3.num_orden)
        # pizzero.tomar_pedido(orden_3.ESTADO_INICIAL)
        # pizzero.tomar_pedido(orden_3.pizzas)

        # #SALIDAS POR CONSOLA
        # #IMPRIMO LA CARTA CON LAS VARIEDADES DE PIZZAS CREADAS
        # print("--------------------------------------------------------------------")
        # print("Carta. ")
        # print(self.carta)

        # #VER LOS NUMEROS DE ORDEN
        # print("--------------------------------------------------------------------")
        # print("Ordenes creadas: ")
        # print(self.ver_ordenes)
        
        # #pizzero.obtener_ordenes_por_cocinar()
        # print("--------------------------------------------------------------------")
        # print("Ordenes tomadas:")
        # print(pizzero.obtener_ordenes_por_cocinar())#[int+["",int]]
        # print("--------------------------------------------------------------------")
        # print( orden_1.obtener_nro_orden())#int
        # print( orden_1.obtener_pizzas())#[""]
        # print("--------------------------------------------------------------------")
        # print( orden_2.obtener_nro_orden())
        # print( orden_2.obtener_pizzas())
        # print("--------------------------------------------------------------------")
        # print( orden_3.obtener_nro_orden())
        # print( orden_3.obtener_pizzas())


        # #COCINAR
        # #pizzero.cocinar()"""

        # #VARIEDAD
       




