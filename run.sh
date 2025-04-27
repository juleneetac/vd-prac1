#!/bin/bash

# Definir rutas al Python y Pip del entorno
VENV_PYTHON="venvolympic/Scripts/python.exe"
VENV_PIP="venvolympic/Scripts/pip.exe"

#Instalar dependencias
echo "Instalando dependencias requirements.txt en el entorno virtual..."
"$VENV_PIP" install -r requirements.txt

# Ejecutar ficheros .py
echo "Ejecutando NOC_codes.py..."
"$VENV_PYTHON" src/NOC_codes.py

echo "Primer script finalizado. Ejecutando main.py..."
"$VENV_PYTHON" src/main.py

echo "Finished =)"

# Opciona: Actualizar requirements.txt manualmente
echo ""
echo "!!!! Si se instalan nuevas librerías, actualiza requirements.txt:"
echo "$VENV_PIP freeze > requirements.txt"