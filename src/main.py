
import pandas as pd
import numpy as np
import pycountry


#~#  Cargar datos
df_code = pd.read_csv("data/countrycode.csv", encoding='latin1')
df_olympic = pd.read_csv("data/olympics.csv")
df_pop0 = pd.read_csv("data/population0_2023.csv")
df_pop60 = pd.read_csv("data/population1960_2023.csv")
df_pop24 = pd.read_csv("data/population2024.csv")
df_noc = pd.read_csv("data/noc.csv", encoding='latin1')

#~# Quitar la columna Team a df_olympic
df_olympic.drop(columns='Team', inplace=True)

#~# Añadir la columna Country a df_olympic con los datos de df_noc
df_olympic = df_olympic.merge(
    df_noc[['NOC_country', 'Country']],
    left_on='NOC',   # Columna en df_olympic
    right_on='NOC_country',         # Columna en df_noc
    how='left'
)
df_olympic.drop(columns='NOC_country', inplace=True)


#~# Añadir la columna Country_code a df_olympic con los datos de df_code
df_olympic = df_olympic.merge(
    df_code[['country_common', 'iso3']],
    left_on='Country',   # Columna en df_olympic
    right_on='country_common',         # Columna en df_code
    how='left'
)
df_olympic.drop(columns='country_common', inplace=True)
df_olympic.rename(columns={'iso3': 'Country_code'}, inplace=True)

# Quitar filas que tengan la columna Country_code vacía
df_olympic = df_olympic.dropna(subset=['Country_code'])


#~# Añadir la columna "Population 2024" del dataset population2024
# Filtrar solo las filas del año 2024
df_2024 = df_olympic[df_olympic['Year'] == 2024]

# Hacemos el merge con df_pop24, que contiene la población de 2024
df_2024 = df_2024.merge(df_pop24[['Country', 'Population 2024']], on='Country', how='left')

# Renombrar la columna para que tenga el nombre que quieres
df_2024 = df_2024.rename(columns={'Population 2024': 'Population_year'})

# Para los años distintos de 2024, el valor de Population_year será NaN
df_rest = df_olympic[df_olympic['Year'] != 2024].copy()
df_rest['Population_year'] = None

# Unir todo
df_olympic_2024 = pd.concat([df_2024, df_rest], ignore_index=True)
df_olympic_2024['Population_year'] = pd.to_numeric(df_olympic_2024['Population_year'], errors='coerce')



#~#Agregar la población de cada país y año (de 1960 a 2023) a df_olympic_2024, 
#~# basándome en las columnas Country_code y Year, pero excluyendo el año 2024.

# Separar filas de 2024 (ya tienen su población)
df_2024 = df_olympic_2024[df_olympic_2024['Year'] == 2024].copy()

# Resto de los años (a los que sí les queremos añadir población)
df_rest = df_olympic_2024[df_olympic_2024['Year'] != 2024].copy()

# Obtener las columnas de años (asegurándote de que sean strings si están como enteros)
year_columns = [str(y) for y in range(1960, 2023)]

# Realizar el melt solo con columnas de años
df_pop60_long = df_pop60.melt(
    id_vars='Country_code',
    value_vars=year_columns,
    var_name='Year',
    value_name='Population_year'
)

# Asegúrate de que Year sea del mismo tipo (probablemente entero)
df_pop60_long['Year'] = df_pop60_long['Year'].astype(int)

# Hacer el merge con los años que van de 1960 a 2023
df_rest = df_rest.merge(
    df_pop60_long,
    on=['Country_code', 'Year'],
    how='left'
)

# Unir todo
df_olympic = pd.concat([df_rest, df_2024], ignore_index=True)

df_olympic['Population_year'] = df_olympic['Population_year'].combine_first(df_olympic['Population_year_y'])
df_olympic.drop(columns=['Population_year_y'], inplace=True)
df_olympic.drop(columns=['Population_year_x'], inplace=True)


#~#Agregar la población de cada país y año (con df_pop0) a df_olympic
# Primero nos aseguramos de que las columnas coincidan en tipo
df_pop0['Year'] = df_pop0['Year'].astype(int)

# Filtrar solo las filas de df_olympic donde Population_year está vacío
df_missing_pop = df_olympic[df_olympic['Population_year'].isna()]

# Hacemos el merge con df_pop0 usando Country_code (Code) y Year como claves
df_filled_pop = df_missing_pop.merge(
    df_pop0,
    left_on=['Country_code', 'Year'],
    right_on=['Code', 'Year'],
    how='left'
)

# Reemplazamos los valores nulos en df_olympic con los nuevos obtenidos
df_olympic.loc[df_olympic['Population_year'].isna(), 'Population_year'] = df_filled_pop['Population (historical)'].values

# (Opcional) Elimina la columna 'Code' si no la necesitas
df_olympic.drop(columns=['Code'], errors='ignore', inplace=True)


#~# Convertir a string las columnas de tipo object restantes
df_olympic['Name'] = df_olympic['Name'].astype('string')
df_olympic['Sex'] = df_olympic['Sex'].astype('string')
df_olympic['Season'] = df_olympic['Season'].astype('string')
df_olympic['City'] = df_olympic['City'].astype('string')
df_olympic['Sport'] = df_olympic['Sport'].astype('string')
df_olympic['Event'] = df_olympic['Event'].astype('string')
df_olympic['Medal'] = df_olympic['Medal'].astype('string')
df_olympic['NOC'] = df_olympic['NOC'].astype('string')
df_olympic['Country'] = df_olympic['Country'].astype('string')
df_olympic['Country_code'] = df_olympic['Country_code'].astype('string')

#~# Sacar info del dataset final
# Información general del dataset
df_olympic.info()
print("-" * 50)

# Dimensiones del dataset
print("Dimensiones del dataset:")
print("Shape (filas, columnas):", df_olympic.shape)
print("Columnas:\n", df_olympic.columns)
print("-" * 50)

# Nulos y valores faltantes
print("Valores nulos por columna:")
print(df_olympic.isna().sum())
print("\nPorcentaje de nulos por columna:")
print(df_olympic.isna().mean() * 100)

# Estadísticas descriptivas
print("Estadísticas descriptivas (todas las columnas):")
print(df_olympic.describe(include='all'))
print("-" * 50)

# Duplicados
print("Número de filas duplicadas:")
print(df_olympic.duplicated().sum())
print("-" * 50)

df_olympic.to_csv('data/out/df_olympic_out.csv', index=False)
print("CSV df_olympic_full.csv guardado")



#~# Comprobar si el codigo de pais iso3 es valido
def is_valid_iso3(code):
    return pycountry.countries.get(alpha_3=code) is not None

df_olympic['valid_code'] = df_olympic['Country_code'].apply(is_valid_iso3)
