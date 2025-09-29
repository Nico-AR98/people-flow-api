Este proyecto implementa la API de gestión de empleados para la startup PeopleFlow, permitiendo registrar, consultar, actualizar y eliminar datos de empleados, además de calcular métricas salariales clave para reportes financieros.

Tecnologías Utilizadas

Framework	Django / Django REST Framework	4.2+
Base de Datos	PostgreSQL	14+
Autenticación	JWT (Simple JWT)	5.5.1+
Gestión de Entorno	Poetry	2.2.1+
Gestor de Versiones Python	Pyenv	2.6.8+


Requisitos Previos

Antes de levantar el proyecto, asegúrate de tener instalados en tu sistema:

    Python 3.9+ (Recomendado debido a las dependencias de Simple JWT).

    Poetry (poetry==2.2.1 o superior).

    Pyenv (pyenv==2.6.8 o superior, si lo usas para gestionar tus versiones de Python).

    PostgreSQL (Servidor de base de datos local).


Instalación y Configuración Local

Sigue estos pasos detallados para configurar y levantar la API en tu máquina.

Paso 1: Clonar el Repositorio

Abre tu terminal y clona el proyecto:
Bash

git clone git@github.com:Nico-AR98/people-flow-api.git
cd people-flow

Paso 2: Configurar la Versión de Python (Usando Pyenv)

Asegúrate de que Pyenv utilice la versión de Python que el proyecto requiere (3.9+).
Bash

# Instala Python 3.9 si no lo tienes
pyenv install 3.9.18 
# Establece 3.9.18 como la versión local para este directorio
pyenv local 3.9.18 


Paso 3: Configurar el Entorno con Poetry

Poetry leerá el archivo pyproject.toml para crear el entorno virtual e instalar las dependencias.

# Crea e instala el entorno virtual con las dependencias
poetry install


Paso 4: Configurar la Base de Datos PostgreSQL
Deberás crear la base de datos y un usuario dedicado para la aplicación:
Accede a la consola de administrador de PostgreSQL:

sudo -u postgres psql

Crea la base de datos y el usuario (reemplaza SQL_DATABASE y SQL_USER por los nombres que usarás en tu .env):

CREATE DATABASE peopleflow_db; 
CREATE USER main_user WITH PASSWORD 'Mate2020'; 

Otorga los permisos necesarios al usuario:
    GRANT ALL PRIVILEGES ON DATABASE peopleflow_db TO main_user;
    \c peopleflow_db 
    GRANT CREATE, USAGE ON SCHEMA public TO main_user; 
    \q


Paso 5: Configurar Variables de Entorno

El proyecto usa el paquete python-dotenv para cargar variables desde un archivo .env.
Crea el archivo .env copiando el env.sample:
cp .env.sample .env

Edita el archivo .env para reflejar la configuración de tu base de datos local:

    BASE_URL=http://localhost:8000
    DEBUG=True
    DJANGO_SECRET_KEY='django-insecure-b69itk1b$i^tq(g!0hsx&k@r743@1462m5qp=mw!p$k%1yg6q0'

    # 🚨 ASEGÚRATE DE USAR LOS VALORES QUE CREASTE EN EL PASO 4
    SQL_USER=main_user
    SQL_PASSWORD=Mate2020 
    SQL_DATABASE=peopleflow_db
    SQL_PORT=5432 # Puerto por defecto de PostgreSQL
    SQL_HOST=localhost # Host por defecto en entorno local


Paso 6: Migrar la Base de Datos y Crear Superusuario
Con el entorno virtual activado (Poetry lo hace automáticamente con poetry run):
Aplicar Migraciones:

poetry run python manage.py migrate

Crear Superusuario (Necesario para probar la autenticación y el admin):
poetry run python manage.py createsuperuser


Ejecución del Proyecto
Una vez que el entorno y la base de datos estén configurados, puedes levantar el servidor de desarrollo de Django:

poetry run python manage.py runserver

La API estará disponible en: http://localhost:8000/

Autenticación (JWT)
Este proyecto implementa autenticación JWT. Todos los endpoints están protegidos y requieren un token de acceso válido.

    Obtener Token (Login):
    Envía una solicitud POST a http://localhost:8000/api/token/ con tu email y password de superusuario (o de cualquier usuario creado).
    JSON

    {
        "email": "tu_email@ejemplo.com",
        "password": "tu_password"
    }

    La respuesta te devolverá los tokens access y refresh.

    Uso en Endpoints:
    Para acceder a cualquier endpoint de la API (como /api/employees/), debes incluir el token access en el encabezado de la solicitud:

    Authorization: Bearer <TOKEN_DE_ACCESO>


Requerimientos Adicionales Incluidos

    Paginación y Filtrado: Implementado en el endpoint de listado.

    Métricas Salariales: El endpoint /api/employees/ devuelve el salario total y el salario promedio de los empleados.

    Administración de Job Position:
    Al tratarse de un campo que será utilizado para filtrar empleados, se decidio declararlo como una clase con una relacion de uno a muchos con la clase Employee para asegurar la consistencia.

    Autenticación Simple (JWT): Implementado con djangorestframework-simplejwt usando email como campo de autenticación.

    Documentación: La API está documentada automáticamente con DRF Spectacular (Swagger/OpenAPI). Accede a: http://localhost:8000/api/schema/swagger-ui/

    Gestión de Dependencias: Usando Poetry.

Uso de la Colección de Postman

Para facilitar la interacción con todos los endpoints (incluida la autenticación y la gestión de empleados/puestos), se proporciona la colección People Flow.postman_collection.json en la raíz del repositorio.

    Importar Colección:
    Abre Postman e importa el archivo JSON.

    Configurar Variables:
    La colección utiliza variables de entorno ({{base_url}}, {{access_token}}, {{employee_id}}, etc.).

        base_url ya está configurada a http://localhost:8000.

        access_token se actualiza automáticamente después de ejecutar la solicitud Access Token con tus credenciales.

        employee_id y job_position_id se capturan automáticamente después de crear un recurso (empleado/puesto) y se usan en las solicitudes de Detail, Edit y Delete.

    Flujo de Pruebas Recomendado:
    Para probar la API, sigue el orden:

        Ejecuta Access Token (con tu username/contraseña) para obtener el JWT.

        Ejecuta Create job position para tener un puesto asignable.

        Ejecuta Create employee. El ID del nuevo empleado se guardará automáticamente.

        Prueba las operaciones List, Detail, Edit y Delete de empleados.


Justificación de la Base de Datos: PostgreSQL vs. MongoDB

Para el sistema de gestión de empleados de PeopleFlow, se optó por PostgreSQL (SQL) en lugar de la preferencia mencionada por MongoDB (NoSQL). Esta decisión se basa en la naturaleza de los datos y en la necesidad de integridad y consistencia. 
En este caso en particular, los datos de un empleado (nombre, apellido, email, puesto, salario, fecha de ingreso) tienen una estructura fija y homogénea. Este tipo de datos no se beneficia de la flexibilidad de NoSQL, sino que requiere una estructura rígida para garantizar que cada registro esté completo y correcto.