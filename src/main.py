
import pandas as pd
import numpy as np


# Cargar datos
# df_code = pd.read_csv("data/countrycode.csv")
df_code = pd.read_csv("data/countrycode.csv", encoding='latin1')
df_olympic = pd.read_csv("data/olympics.csv")
df_pop60 = pd.read_csv("data/population1960_2023.csv")
df_pop24 = pd.read_csv("data/population2024.csv")
df_noc = pd.read_csv("data/noc.csv", encoding='latin1')

print(df_code.head())
print(df_olympic.head())

## Añadir country code 
print(df_noc.head())

# Hacemos el merge usando NOC (df_olympic) e iso3 (df_code) 
df_olympic = df_olympic.merge(df_noc[['NOC', 'Country']], on='NOC', how='left')

print(df_olympic.head())


##########
# # Hacemos merge para añadir la columna iso3
# df_olympic = df_olympic.merge(df_code[['country_common', 'iso3']], left_on='Team', right_on='country_common', how='left')

# # Opcional: eliminar columna auxiliar si ya no se necesita
# df_olympic = df_olympic.drop(columns=['country_common'])

# df_nan = df_olympic[df_olympic['iso3'].isna()]['Team'].unique()

# print(df_olympic.head())

# print(df_nan)


################

# # Hacemos el merge usando NOC (df_olympic) e iso3 (df_code) 
# df_olympic_merged = df_olympic.merge(df_code[['noc', 'country_common']], left_on='NOC', right_on='iso3', how='left')

# # Reemplazamos la columna 'Team' por 'country_common'
# df_olympic_merged['Team'] = df_olympic_merged['country_common']

# # Si quieres, puedes eliminar las columnas auxiliares
# df_olympic_merged = df_olympic_merged.drop(columns=['iso3', 'country_common'])

# print(df_olympic_merged.head())