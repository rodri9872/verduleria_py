
import os

def datosFijos(): #carga de datos fijos
    lista_actualizada = (
        "manzana", 230, 
        "naranja", 150,     
        "banana", 180, 
        "pera", 300,
        "uva", 120,
        "palta", 75 
    )
    lista_articulos = {} 
    lista_precios = {}
    j=0
    for i in range(0,len(lista_actualizada),2):
        j=j+1
        # print(i,j)
        agregaArticulos={j:lista_actualizada[i]}
        lista_articulos.update(agregaArticulos)
        agregaPrecios={j:lista_actualizada[i+1]}
        lista_precios.update(agregaPrecios)

    return [lista_articulos,lista_precios]

def menu(art, prec):
    print('ARTICULOS   -   PRECIO')
    print('----------------------')
    for i in range(len(art)):
        print('{0:>1} - {1:<10} {2} {3:>4}'.format(i+1,art[i+1],':$',prec[i+1]))
        
    return
    
def compra_EnProceso(art, prec, cant, formato):
    resultado = 0
    for nro_articulo, cantidad in cant.items():
        print(formato.format(art[nro_articulo], cantidad ,prec[nro_articulo],(cantidad * prec[nro_articulo] ) ))
        resultado = resultado + (cantidad * prec[nro_articulo])

    return resultado

def comprado(art, prec, cant, formato):
    print('ARTICULOS  CANT      PRECIO UNIT  TOTAL')
    print('----------------------------------------------')
    
    return compra_EnProceso(art, prec, cant, formato)

    
def ticket(art, prec, cant, formato):
    os.system("cls")
    print('TICKET - VERDULERÍA "LA PAPA"')
    print('==============================================')
    total = comprado(art, prec, cant, formato)
    print("===================")
    print("TOTAL: $", total)
    print("===================")
