# Proyecto de Gestión de Turnos de Compra y Venta de Vehículos

Este proyecto es un sistema CRUD para gestionar un sistema de turnos de compra y venta de vehículos, desarrollado en Python utilizando FastAPI y SQLAlchemy.

## Requisitos Previos

Tener instalados los siguientes requisitos en tu máquina:

- Python 3.8+
- MySQL
- Git

## Clonar el Proyecto

Para clonar el proyecto, ejecuta el siguiente comando en tu terminal:

```bash
git clone https://github.com/renzo611/auta_challenge.git
```
# Configuración del Entorno

## Ingresa al proyecto con tu editor de codigo preferido

## Crea y activa un entorno virtual
En este caso se uso PyCharm lo cual el siguiente paso no es necesario
```bash
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows
```

## Instala las dependencias necesarias
```bash
pip install -r libraries.txt
```

# Variables de Entorno

Crea un archivo .env en la raíz del proyecto y configura las siguientes variables de entorno:
```bash
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=auda_database
```


# Configuración de la Base de Datos
Crea la base de datos y las tablas, y carga los datos de prueba ejecutando el script database.sql dentro de su gestor de base de datos favorito


# Ejecutar el Proyecto
```bash
uvicorn main:app --reload
```

# Notas
- Una vez ejecutado el proyecto este utilizara el puerto 8080 como puerto de respuesta.
- Para visualizar todos los endpoints disponibles puede acceder al siguiente enlace http://127.0.0.1:8000/docs donde podra visualizar la documentacion basica de Swagger.
- Hay tres secciones disponibles (Clients, Vehicles y Appointments), donde cada uno contiene las operaciones basicas de un CRUD de cada entidad.
- Dentro de los enpdoins disponibles hay una seccion llamada First exercise que contiene un endpoint que resuelve el primer ejericio del challenge.
