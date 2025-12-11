#!/bin/bash
set -e  # Detener si hay error

echo "=================================================="
echo "Iniciando instalación de dependencias"
echo "=================================================="

pip install -r requirements.txt

echo ""
echo "=================================================="
echo "Ejecutando script de build Python"
echo "=================================================="

python3.9 vercel_build.py

echo ""
echo "=================================================="
echo "Build completado!"
echo "=================================================="