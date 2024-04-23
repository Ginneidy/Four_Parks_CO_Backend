````
# Four Parks CO Backend

Este proyecto consiste en el desarrollo de un sistema de gestión de parqueaderos que permite a los usuarios reservar espacios de estacionamiento, administrar sus reservas, realizar pagos y acceder a información detallada sobre los parqueaderos disponibles.

## Requisitos Previos

- Python >= 3.x
- PostgreSQL
- Pip (administrador de paquetes de Python)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/londono27/Four-Park-CO.git
   ````

2. Ve al directorio del proyecto:

   ```bash
   cd directorio del proyecto Four-Park-CO
   ```

3. Crea y activa un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv `nombre_para_el_entorno_virtual`
   django_venv\Scripts\activate  # Windows
   ```

4. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

5. Configura la base de datos en PostgreSQL:
   https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
   -  Crea una base de datos en PostgreSQL para el proyecto.
   -  Actualiza las configuraciones de la base de datos en `settings.py` con las credenciales de tu base de datos PostgreSQL.
   - DATABASES = {
      "default": {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": env("DB_NAME"),
         "USER": env("DB_USER"),
         "PASSWORD": env("DB_PASSWORD"),
         "HOST": env("DB_HOST"),
         "PORT": env("DB_PORT"),
         }  
      }


6. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

8. Abre tu navegador web y accede a `http://localhost:8000/` o el que aparezca en consola para ver la aplicación en funcionamiento.
