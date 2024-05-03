import pandas as pd

#Obtenemos la lista de calificaciones
calificaciones = [ {"nombre": "Juan", "matematicas": 85, "ciencias": 90,
"historia": 75}, {"nombre": "María", "matematicas": 70, "ciencias": 80,
"historia": 85}, {"nombre": "Pedro", "matematicas": 95, "ciencias": 75,
"historia": 90}, {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia":
80}, {"nombre": "Luis", "matematicas": 75, "ciencias": 70,
"historia": 95}, {"nombre": "Sofía", "matematicas": 90, "ciencias": 85,
"historia": 75}, {"nombre": "Carlos", "matematicas": 85, "ciencias": 90,
"historia": 80}, {"nombre": "Elena", "matematicas": 70, "ciencias": 75,
"historia": 85}, {"nombre": "Javier", "matematicas": 80, "ciencias": 85,
"historia": 90}, {"nombre": "Laura", "matematicas": 75, "ciencias": 70,
"historia": 95}, {"nombre": "Diego", "matematicas": 90, "ciencias": 85,
"historia": 75}, {"nombre": "Paula", "matematicas": 85, "ciencias": 90,
"historia": 80}, {"nombre": "Carmen", "matematicas": 70, "ciencias": 75,
"historia": 85} ]

#Transformamos la lista en un dataframe
df = pd.DataFrame(calificaciones, columns=["nombre", "matematicas", "ciencias", "historia"])
print("Planilla de calificaciones")
print(df)

print("--"*30)#Linea de separación. Para prolijidad y presentación.

#Calcular el promedio para cada asignatura utilizando la función mean()
print("Nota promedio de todos los alumnos")
print("Promedio de Matematicas")
print(df["matematicas"].mean())


print("Promedio de Ciencias")
print(df["ciencias"].mean())



print("Promedio de Historia")
print(df["historia"].mean())

print("--"*30)

#Encontramos la nota mas alta de cada materia y su alumno
#Matemática

print("Calificacion mas alta matematica")
def detectar_calif_alta_mate(df):
    calif_alta_mate = df['matematicas'].max() #Encontramos el valor mas alto de la columna "matematicas"
    for index, row in df.iterrows(): #Con la funcion iterrows() iteramos sobre cada fila para buscar la calif mas alta.
        if row['matematicas']== calif_alta_mate:
            print(row['nombre'])
            print(calif_alta_mate)
detectar_calif_alta_mate(df)


#Ciencias (repite la lógica de la función anterior)
print("Calificacion mas alta ciencias")
def detectar_calif_alta_ciencias(df):
    calif_alta_ciencias = df['ciencias'].max() #Encontramos el valor mas alto de la columna "matematicas"
    for index, row in df.iterrows():
        if row['ciencias']== calif_alta_ciencias:
            print(row['nombre'])
            print(calif_alta_ciencias)
detectar_calif_alta_ciencias(df)

#Historia (misma lógica de búsqueda de nota alta)
print("Calificacion mas alta historia")
def detectar_calif_alta_historia(df):
    calif_alta_historia = df['historia'].max() #Encontramos el valor mas alto de la columna "matematicas"
    for index, row in df.iterrows():
        if row['historia']== calif_alta_historia:
            print(row['nombre'])
            print(calif_alta_historia)
detectar_calif_alta_historia(df)

print("--"*30)

#Calcular el porcentaje de alumnos aprobados de cada asignatura
#Matematica
print("Porcentaje de aprobados en Matematica")
def porcentaje_aprobados_mate(df):
    #Variables de utilidad.
    aprobados = 0
    total_alumnos= len(df)
    calif_aprobar = 60

    for nota, row in df.iterrows():
        if row['matematicas']>= calif_aprobar: #Comparar si en la iteración, la nota cumple la aprobación de >= 60
            aprobados += 1
    porcentaje_aprobados_mate = (aprobados*100)/total_alumnos #Si lo hace, calcula el porcentaje de los aprobados.
    return porcentaje_aprobados_mate
print(porcentaje_aprobados_mate(df))

#Ciencias (repite lógica de la función anterior)
print("Porcentaje de aprobados en Ciencias")
def porcentaje_aprobados_ciencias(df):
    aprobados = 0
    total_alumnos= len(df)
    calif_aprobar = 60

    for nota, row in df.iterrows():
        if row['ciencias']>= calif_aprobar:
            aprobados += 1
    porcentaje_aprobados_ciencias = (aprobados*100)/total_alumnos
    return porcentaje_aprobados_ciencias
print(porcentaje_aprobados_ciencias(df))

#Historia (misma lógica para calcular el porcentaje de aprobados)
print("Porcentaje de aprobados en Historia")
def porcentaje_aprobados_histo(df):
    aprobados = 0
    total_alumnos= len(df)
    calif_aprobar = 60

    for nota, row in df.iterrows():
        if row['historia']>= calif_aprobar:
            aprobados += 1
    porcentaje_aprobados_histo = (aprobados*100)/total_alumnos
    return porcentaje_aprobados_histo
print(porcentaje_aprobados_histo(df))

#Crear un DataFrame de dos columnas: Estudiante y promedio de sus notas.
print("--"*30)
print("Dataframe con el promedio de notas de alumnos")
#Calcular promedio de notas
def promedio_notas(df):
    promedio_notas = []
    for index, row in df.iterrows():
            promedio_notas.append('matematicas')
            promedio_notas.append('ciencias')
            promedio_notas.append('historia')
    promedio_notas = sum(promedio_notas) / len(promedio_notas)
    return promedio_notas

df2 = pd.DataFrame(calificaciones, columns=['nombre', 'promedio_notas'])
print(df2)