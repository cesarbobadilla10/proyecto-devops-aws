import boto3
import time

REGION = "us-east-1"
TABLE_NAME = "devops-tabla"

dynamodb = boto3.resource("dynamodb", region_name=REGION)
client = boto3.client("dynamodb", region_name=REGION)


def crear_tabla():
    tablas = client.list_tables()["TableNames"]

    if TABLE_NAME in tablas:
        print(f"La tabla {TABLE_NAME} ya existe.")
        return dynamodb.Table(TABLE_NAME)

    print(f"Creando tabla {TABLE_NAME}...")

    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    table.wait_until_exists()
    print("Tabla creada correctamente.")
    return table


def insertar_registro(table):
    print("Insertando registro...")

    table.put_item(
        Item={
            "id": "1",
            "nombre": "registro-devops",
            "status": "creado"
        }
    )

    print("Registro insertado correctamente.")


def modificar_registro(table):
    print("Modificando registro...")

    table.update_item(
        Key={
            "id": "1"
        },
        UpdateExpression="SET #st = :nuevo_status",
        ExpressionAttributeNames={
            "#st": "status"
        },
        ExpressionAttributeValues={
            ":nuevo_status": "actualizado"
        }
    )

    print("Registro actualizado correctamente.")


def eliminar_registro(table):
    print("Eliminando registro...")

    table.delete_item(
        Key={
            "id": "1"
        }
    )

    print("Registro eliminado correctamente.")


if __name__ == "__main__":
    tabla = crear_tabla()
    time.sleep(2)
    insertar_registro(tabla)
    modificar_registro(tabla)
    eliminar_registro(tabla)
    print("Operaciones de DynamoDB completadas.")
