from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "fourParks",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

]


CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
# Send email

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "fourparksdsp@gmail.com"
EMAIL_HOST_PASSWORD = "ihyb omyz fkwa fjbw"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
