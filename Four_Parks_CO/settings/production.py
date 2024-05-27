from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "fourParks",
        "USER": "avnadmin",
        "PASSWORD": "AVNS_lbb15Vs7IkJnNCFD6c7",
        "HOST": "pg-48e5b0c4-e8a5-456f-b213-5a6b94abe153-fourpark3518781457-chor.i.aivencloud.com",
        "PORT": "26810",
    }
}
