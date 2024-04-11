import pandas as pd
print("Inicio")
df =pd.read_excel("datos_facturacion.xlsx")
print(df.head())

filtro1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
print(filtro1)
filtro1.to_csv("practica_facturacion_1.csv")

filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
print(filtro2)

df['FECHAELAB'] = pd.to_datetime(df['FECHAELAB'])
filtro3=df[df["FECHAELAB"].dt.strftime('%Y-%m-%d') == '2019-10-02']
print(filtro3)

filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
print(filtro4)

filtro5 = df.iloc[ : , [0, 6, 7,9]]  
print(filtro5)

filtro6 = df.iloc[7001:7099, :  ] 
print(filtro6)

df1= pd.read_excel('datos_facturacion.xlsx', index_col=3)
df1.head()

filtro7=df1.loc[[1.0,2.0], ["FECHAELAB"]]
print(filtro7)


filtro1.to_csv("Entregable1.1.csv")
filtro2.to_csv("Entregable2.1.csv")
filtro3.to_csv("Entregable3.1.csv")
filtro4.to_csv("Entregable4.1.csv")
filtro5.to_csv("Entregable5.1.csv")
filtro6.to_csv("Entregable6.1.csv")
filtro7.to_csv("Entregable7.1.csv")