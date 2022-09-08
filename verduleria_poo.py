from verduleria_stock import datosFijos

# ----- prog. principal ----------
resultados = datosFijos()  #carga de datos fijos
articulos=resultados[0]
precios=resultados[1]
cantidades={}
total = 0
formato_columna = '{0:<10} {1:<2}kg.      :$ {2:<4}     $ {3:<12}'
print(articulos,precios)