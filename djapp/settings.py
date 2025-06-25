import os

SECRET_KEY = "dummy"
DEBUG = True
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "djapp.urls"
INSTALLED_APPS = []
MIDDLEWARE = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3" if not os.environ.get("DATABASE_URL") else "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_URL", "db.sqlite3"),
    }
}
