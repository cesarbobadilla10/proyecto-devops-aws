import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Microservicio DevOps funcionando correctamente",
        "Despliegue automatizado en AWS completado",
        "Monitoreo y automatización activos",
        "Proyecto DevOps ejecutándose desde Lambda",
        "Infraestructura serverless disponible"
    ]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "mensaje": random.choice(mensajes),
            "servicio": "microservicio-devops"
        })
    }
