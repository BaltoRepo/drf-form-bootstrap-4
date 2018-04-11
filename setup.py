import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='drf-form-bootstrap-4',
    version='0.1',
    packages=['drfformbootstrap4'],
    description='Bootstrap 4 templates for Django Rest Framework `render_form` tag',
    long_description=README,
    author='Matt Fox',
    author_email='matt@tansen.ca',
    url='https://github.com/mattfox/drf-form-bootstrap-4',
    license='MIT',
    install_requires=[
        'Django',
        'djangorestframework',
    ],
    tests_require=[
        'django-fake-model',
    ],
    zip_safe=False,  # Zipping prevents Django from finding migrations.
    include_package_data=True,
)
