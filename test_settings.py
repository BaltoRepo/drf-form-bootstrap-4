INSTALLED_APPS = (
    'drfformbootstrap4',
    'rest_framework',
    'django.contrib.contenttypes',
    'django.contrib.auth',
)
# We don't need no persistence, so use SQLite in-memory DB.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
SECRET_KEY = "1234567890!@#$%^&*()qwerty"
ROOT_URLCONF = 'drfformbootstrap4.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]
