"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

import os
import os.path

from django.utils.translation import gettext_lazy as _

from decouple import config


###############################################################################
### PRODUCT VERSIONS                                                        ###
###############################################################################
PRODUCT_NAME = "ddaemon-infra"

# --- Versioning Strategy
#     <major>.<minor>.<patch>

VERSION_API = "v1"
VERSION_MAJOR = 0
VERSION_MINOR = 0
VERSION_PATCH = 0

PRODUCT_VERSION= f"v.{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"


###############################################################################
### BASIC SETTINGS                                                          ###
###############################################################################
DEBUG = config("DEBUG", default=False, cast=bool)
DEBUG_TOOLBAR = True

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",))
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
DJANGO_SETTINGS_MODULE = config("DJANGO_SETTINGS_MODULE", default="settings.dev")

ADMINS = (
    ("Artem Suvorov", "artem.suvorov@gmail.com"),
)
MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE":   config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME":     config("DB_NAME", default="sqlite.db"),
        "USER":     config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST":     config("DB_HOST", default=""),
        "PORT":     config("DB_PORT", default=""),
        "OPTIONS": {
            # "autocommit": True,
        }
    }
}

DOMAIN_NAME = "example.com"
ALLOWED_HOSTS = ["*"]
APPEND_SLASH = True

TIME_ZONE = "America/Los_Angeles"

LANGUAGE_CODE = "en-us"
LANGUAGES = (
    ("en",  _("English")),
    ("de",  _("Deutsch")),
    ("es",  _("Spanish")),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "locale"),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMIN_MEDIA_PREFIX = "/static/admin/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "staticserve")
STATICFILES_DIRS = (
    ("", f"{PROJECT_PATH}/static"),
)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
)

SECRET_KEY = config("SECRET_KEY", default="@zew8t_wcz!qn9=8+hheltx@&b#!x@i6ores96lhbnobr3jp*c")
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)

TEMPLATES = [
    {
        "BACKEND":  "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_PATH, "templates/"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug":    DEBUG,
            # "loaders": [
            #     "django.template.loaders.filesystem.Loader",
            #     "django.template.loaders.app_directories.Loader",
            # ],
            "context_processors": [
                "django.template.context_processors.csrf",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


###############################################################################
### DJANGO MIDDLEWARE CLASSES                                               ###
###############################################################################
MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "urls"

WSGI_APPLICATION = "wsgi.application"

INSTALLED_APPS = (
    # --- Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # --- 3rd Party Apps

    # --- Project Apps
    "api",
    "app",
)

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"


###############################################################################
### DJANGO CACHING                                                          ###
###############################################################################
CACHES = {
    "default": {
        "BACKEND":  "django.core.cache.backends.dummy.DummyCache",
    },
    "some-other-cache": {
        "BACKEND":  "django.core.cache.backends.dummy.DummyCache",
    },
}


###############################################################################
### DJANGO LOGGING                                                          ###
###############################################################################
LOGGING = {
    "version":                      1,
    "disable_existing_loggers":     False,
    "filters": {
        "require_debug_false": {
            "()":                   "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()":                   "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "simple": {
            "format":               "[%(asctime)s] %(levelname)s %(message)s",
            "datefmt":              "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format":               "[%(asctime)s] %(levelname)s "
                                    "[%(name)s.%(funcName)s:%(lineno)d] "
                                    "%(message)s",
            "datefmt":              "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level":                "INFO",
            "filters": [
                "require_debug_true",
            ],
            "class":                "logging.StreamHandler",
            "formatter":            "simple",
        },
        "null": {
            "class":                "logging.NullHandler",
        },
        "mail_admins": {
            "level":                "ERROR",
            "filters": [
                "require_debug_false",
            ],
            "class":                "django.utils.log.AdminEmailHandler",
            "formatter":            "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": [
                "console",
            ],
        },
        "django.request": {
            "handlers": [
                "mail_admins",
            ],
            "level":                "ERROR",
            "propagate":            False,
        },
        "py.warnings": {
            "handlers": [
                "console",
            ],
        },
    },
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)
AUTH_USER_MODEL = "User"
