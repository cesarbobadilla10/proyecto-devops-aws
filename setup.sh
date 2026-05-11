#!/bin/bash

echo "Actualizando paquetes del sistema..."
sudo dnf update -y

echo "Instalando dependencias de Python..."
pip3 install boto3 --user

echo "Verificando instalaciones..."
python3 --version
pip3 show boto3

echo "Configuración inicial completada."
