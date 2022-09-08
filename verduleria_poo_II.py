from verduleria_stock import datosFijos, menu, compra_EnProceso, ticket
class Venta():
    def __init__(self):
        stock_valorizado = datosFijos()
        self.__articulos = stock_valorizado[0]
        self.__precios = stock_valorizado[1]
        self.cantidades={}
        self.total = 0
        self.__formato_columna = '{0:<10} {1:<2}kg.      :$ {2:<4}     $ {3:<12}'
        

    def armoTicket(self):
        menu(self.__articulos,self.__precios)

    def sleccionarticulos(self):
    	while True:
    		nro_articulo = input('SELECCIONE UNA OPCION (x para terminar) =>')  #cargar opcion y validar la entrada
    		if nro_articulo.lower() == "x": #salir dada cierta condicion
    			ticket1=self.ticketcompra()
    			break
    		if int(nro_articulo) > 0 and int(nro_articulo) <= len(self.__articulos):

    			try:
    				self.cantidades[int(nro_articulo)] = int(input("Ingresa la cantidad de " + self.__articulos[int(nro_articulo)] + ":"))
    				compra_EnProceso(self.__articulos, self.__precios, self.cantidades, self.__formato_columna)
    				#mostrar lo comprado
    			except ValueError:
    				print("ingrese una cantidad valida")
    		else:
    			a=input("No es una opción valida-presione ENTER para continuar")
    		


    def ticketcompra(self):
    	ticket(self.__articulos, self.__precios, self.cantidades, self.__formato_columna)

# ----- prog. principal ----------


venta1 = Venta()
venta1.armoTicket()
venta1.sleccionarticulos()


