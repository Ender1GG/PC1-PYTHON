
import pandas as pd
import sqlite3
import json

df = pd.read_csv("./data/winemag-data-130k-v2.csv")

print(df.info())
print(df.head())


df = df.rename(columns={
    'country': 'pais',
    'description': 'descripcion',
    'points': 'puntos',
    'price': 'precio',
    'variety': 'tipo_uva'
})


df['rango_precio'] = pd.cut(df['precio'], bins=[0, 20, 50, 100, 1000],
                            labels=['Económico', 'Medio', 'Alto', 'Premium'])


df['puntos_por_precio'] = df['puntos'] / df['precio']


df['calidad'] = pd.cut(df['puntos'], bins=[0, 85, 90, 95, 100],
                       labels=['Regular', 'Buena', 'Muy buena', 'Excelente'])


reporte1 = df.groupby('pais').agg({'precio': 'mean', 'descripcion': 'count'}).rename(columns={'descripcion': 'cantidad_vinos'})
reporte1.to_csv('reporte1.csv')
print("Reporte 1 generado: reporte1.csv")


reporte2 = df.loc[df.groupby('pais')['puntos'].idxmax()].sort_values(by='puntos', ascending=False)
reporte2.to_excel('reporte2.xlsx', index=False)
print("Reporte 2 generado: reporte2.xlsx")

reporte3 = df['rango_precio'].value_counts().reset_index()
reporte3.columns = ['rango_precio', 'cantidad']
conn = sqlite3.connect('reporte3.sqlite')
reporte3.to_sql('reporte3', conn, index=False, if_exists='replace')
conn.close()
print("Reporte 3 generado: reporte3.sqlite")


reporte4 = df['calidad'].value_counts().reset_index()
reporte4.columns = ['calidad', 'cantidad']
with open('reporte4_mongo.json', 'w') as f:
    json.dump(reporte4.to_dict(orient='records'), f, indent=4)
print("Reporte 4 generado: reporte4_mongo.json (formato compatible con MongoDB)")
