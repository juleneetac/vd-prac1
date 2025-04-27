# PRAC1 - Proyecto de visualización
PRAC1 - Visualización de Datos - Data Science - UOC

## Autores
Julen

## Estructura del proyecto
+ /src/
    - main.py: archivo desde donde se ejecuta el código principal
    - NOC_codes.py: lógica para pasar la lista de país y código NOC a csv

+ /data/
    - countrycode.csv: [Kaggle, Country Codes (ISO 3166)](https://www.kaggle.com/datasets/wbdill/country-codes-iso-3166)
    - noc.csv: CSV resultante de ejecutar el fichero NOC_codes.py
    - olympics.csv: [Kaggle, Summer Olympics Medals (1896-2024)](https://www.kaggle.com/datasets/stefanydeoliveira/summer-olympics-medals-1896-2024)
    - population0_2023.csv: [Our World in Data, Population](https://ourworldindata.org/grapher/population)
    - population1960_2023.csv: [Kaggle, World population from 1960 to 2023](https://www.kaggle.com/datasets/fredericksalazar/population-world-since-1960-to-2021)
    - population2024.csv: [Kaggle, World Population by country 2024](https://www.kaggle.com/datasets/dataanalyst001/world-population-by-country-2024)
    - /out/:  
        -- df_olympic_out.csv: CSV resultante de ejecutar main.py. Dataset con el que se realizará la visualización.

+ README.md: contiene información útil respecto al proyecto, como quienes son sus autores o como se ejecuta.

+ requirements.txt:  librerías necesarias para ejecutar el código.

+ .gitignore: se añaden los archivos que no se quieren incluir en el repositorio

+ LICENSE: Licencia de código abierto "GNU General Public License v3.0"

## Instalación

**1. Creación del entorno virtual**
Si es la primera vez que se usa este proyecto,
en el terminal se lanzará el siguiente comando:

```shell
python -m venv venvolympic
```
**2. Ejecución del programa**
```shell
bash run.sh
```
o
```shell
.\run.sh
```
----------------------------------------------------------------------------
## Alternativa, en caso de error

Si al ejecutar el fichero run.sh diera algún error, habría que ejecutar el entorno manualmente.
Despuñes del paso "1. Creación del entorno virtual", ejecutar lo siguiente:

**2. Activación del entorno virtual**
```shell
venvolympic\Scripts\activate
```

**3. Instalar requirements**
```shell
pip install -r requirements.txt
```

## Instrucciones para el Run

**4. Ejecución del main**
```shell
4.1.  
python src/NOC_codes.py

4.2.  
python src/main.py
```

**5. (Opcional) Antes de subir el codigo a git, hacer update del requirements.txt**
```shell
pip freeze > requirements.txt
```
