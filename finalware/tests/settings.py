import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "un33k"

TEMPLATE_DIRS = [
    '%s' % os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
]

# Static file finders in order of precedence
# #####################################
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

# Template
# #####################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': ['./finalware/tests/templates'],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.csrf',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'finalware.context_processors.contextify',
            ],
            # 'loaders': (
            #     ('django.template.loaders.cached.Loader', (
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #         )),
            # ),
            # 'buildins': SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST,
        },
    },
]

# Middleware classes
# #####################################
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Installed Apps
# #####################################
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.admin',


    # last application to finalize things
    'finalware',
]

# Site objects auto config
# #####################################
# site info (you need at least one site)
SITE_OBJECTS_INFO_DICT = {
    '1': {
        'name': 'production',
        'domain': 'example.com',
    },
    '2': {
        'name': 'integration',
        'domain': 'example.org'
    },
    '3': {
        'name': 'development',
        'domain': '192.168.1.20:8080'
    },
}
SITE_ID = 1

ROOT_URLCONF = 'finalware.tests.urls'
STATIC_URL = '/s/'

SITE_ENABLE_SESSION_IN_ADMIN = True

SITE_SUPERUSER_USERNAME = 'admin'
SITE_SUPERUSER_EMAIL = 'admin@example.com'
SITE_SUPERUSER_PASSWORD = 'coolpass'

SITE_EXTRA_CONTEXT_DICT = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST = [
    # django tags
    'django.templatetags.cache',
    'django.templatetags.future',
    'django.templatetags.i18n',
    'django.templatetags.l10n',
    'django.templatetags.static',
    'django.contrib.humanize.templatetags.humanize',
]
