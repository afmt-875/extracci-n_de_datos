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

#Mandar a csv
filtro1.to_csv("Entregable1.cvs")
filtro2.to_csv("Entregable2.cvs")
filtro3.to_csv("Entregable3.cvs")