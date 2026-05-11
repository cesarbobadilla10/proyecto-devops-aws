#!/bin/bash

LOG_DIR="$HOME/environment/proyecto-devops-aws/logs"

echo "Iniciando limpieza de logs..."

mkdir -p "$LOG_DIR"

find "$LOG_DIR" -type f -name "*.log" -mtime +7 -delete

echo "Limpieza de logs completada: $(date)" >> "$LOG_DIR/limpieza.log"
