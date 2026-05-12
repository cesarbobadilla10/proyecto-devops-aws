import boto3
from datetime import datetime

BUCKET_NAME = "devops-bucket-588523411497"
FILE_NAME = "archivo_prueba.txt"
S3_KEY = f"pruebas/{FILE_NAME}"

s3 = boto3.client("s3", region_name="us-east-1")


def crear_archivo_local():
    with open(FILE_NAME, "w") as archivo:
        archivo.write("Archivo de prueba para automatización S3.\n")
        archivo.write(f"Fecha de creación: {datetime.now()}\n")

    print(f"Archivo local creado: {FILE_NAME}")


def subir_archivo_s3():
    s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)
    print(f"Archivo subido a s3://{BUCKET_NAME}/{S3_KEY}")


def listar_objetos_bucket():
    print(f"\nObjetos dentro del bucket {BUCKET_NAME}:")

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if "Contents" not in response:
        print("No hay objetos en el bucket.")
        return

    for objeto in response["Contents"]:
        nombre = objeto["Key"]
        tamano = objeto["Size"]
        fecha = objeto["LastModified"]

        print(f"- {nombre} | Tamaño: {tamano} bytes | Modificado: {fecha}")


if __name__ == "__main__":
    crear_archivo_local()
    subir_archivo_s3()
    listar_objetos_bucket()
