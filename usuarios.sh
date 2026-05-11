#!/bin/bash

echo "Creando grupo devops..."
sudo groupadd devops_group 2>/dev/null || echo "El grupo devops_group ya existe."

echo "Creando usuario devops_user..."
sudo useradd -m -G devops_group devops_user 2>/dev/null || echo "El usuario devops_user ya existe."

echo "Asignando permisos al directorio del proyecto..."
sudo chown -R devops_user:devops_group ~/environment/proyecto-devops-aws

echo "Restaurando permisos para ec2-user en ~/environment..."
sudo chown -R ec2-user:ec2-user ~/environment

echo "Usuarios y permisos configurados correctamente."
