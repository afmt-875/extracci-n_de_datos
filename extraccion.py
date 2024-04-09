import pandas as pd
print("Aplicación de Extracción de Datos")
df = pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx")
#print(df.info())
print(df.head())                  

#Filtro por objeto
filtro1 = df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
print(filtro1.head())

#Filtro por filas
filtro2 = df.iloc[2:8,: ]
print(filtro2)

#Filtro por columnas
filtro3 = df.iloc[: , [1,3,4,10]]
print(filtro3.head())

#Filtro por filas con columnas
df1= pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx', index_col=1)
filtro4=df1.loc[["2022-11-22","'2022-12-23"], ["SUBTOTAL_PARTIDA"]]
print(filtro4.head())

#Filtrar para que muestre los primeros n registros
filtro5 = df.head(8)
print(filtro5.head())

#Filtrar por comparación
filtro6 = df[df["SUBTOTAL_PARTIDA"] > 77000]
print(filtro6.head())

#Realizar una doble condición para filtrar
filtro7 = df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
print(filtro7.head())

#Realizar una condición u otra para filtrar
filtro8 = df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
print(filtro8.head())

#Filtro condición not
filtro9 = df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
print(filtro9.head())

#Mandar a csv
filtro1.to_csv("Entregable1.cvs")
filtro2.to_csv("Entregable2.cvs")
filtro3.to_csv("Entregable3.cvs")
filtro4.to_csv("Entregable4.cvs")
filtro5.to_csv("Entregable5.cvs")
filtro6.to_csv("Entregable6.cvs")
filtro7.to_csv("Entregable7.cvs")
filtro8.to_csv("Entregable8.cvs")
filtro9.to_csv("Entregable9.cvs")