import numpy as np
import pandas as pd

# Ejercicio 2 - Enunciado.
# A partir del siguiente diccionario:
data = {
    "nombres": [
        "Fran", "Rober", "Alba", "Luz", "Evan",
        "Marc", "Luis", "Jesus","Leo","Nael"
    ],
    "deportes": [
        "Futbol", "Baloncesto", "Tenis", "Baloncesto",
        "Baloncesto","Futbol","Tenis",
        "Tenis", "Futbol", "Futbol"
    ]
}

# Crear un dataframe de la variable data y a continuación realizar las operaciones necesarias para imprimir
# por pantalla los nombres de las personas asociados a cada deporte.
df = pd.DataFrame(data)

unique_sports = df['deportes'].unique()
for sport in unique_sports:

    nombres_deporte = df[df['deportes'] == sport]['nombres']
    array_dep = np.array(nombres_deporte)
    print(f'{sport} : {', '.join(array_dep)}.')

# Ejercicio 3 - Enunciado.
# A partir del siguiente fichero csv

# tienda,cod_producto,stock_producto,coste_producto,precio_producto
# tienda1,1,100,200,350
# tienda1,2,32,800,1100
# tienda1,3,85,400,500
# tienda2,1,10,220,550
# tienda2,2,7,850,1200
# tienda2,3,5,450,550

# Importarlo en un dataframe de pandas y calcular para cada tienda:
#
# •El stock medio y el precio medio de sus productos.
# Un ejemplo de posible resultado sería:
df = pd.read_csv('datos.csv')

for tienda, group in df.groupby('tienda'):
    stock_medio = round(group['stock_producto'].mean(), 5)
    precio_medio = round(group['precio_producto'].mean(), 5)
    print(f'Tienda: {tienda}, Stock medio: {stock_medio}, Precio medio: {precio_medio}')
