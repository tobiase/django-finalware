DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "un33k"

# Static file finders in order of precedence
#######################################
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

# Template file loads in order of precedence
#######################################
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
]

# Context processor
#######################################
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',

    'finalware.context_processors.contextify',
]

# Installed Apps
#######################################
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
#######################################
# site info (you need at least one site)
SITE_OBJECTS_INFO_DICT = {
    '1': {
        'name': 'production',
        'domain': 'example.com',
    },
    '2':{
        'name': 'integration',
        'domain': 'example.org'
    },
    '3':{
        'name': 'development',
        'domain': '192.168.1.20:8080'
    },
}
SITE_ID = 1

ROOT_URLCONF = 'finalware.tests.urls'
STATIC_URL = '/s/'