import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='drf-form-bootstrap-4',
    version='0.5.3',
    packages=['drfformbootstrap4'],
    description='Bootstrap 4 templates for Django Rest '
                'Framework `render_form` tag',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Matt Fox',
    author_email='matt@getbalto.com',
    url='https://github.com/BaltoRepo/drf-form-bootstrap-4',
    license='MIT',
    install_requires=[
        'Django',
        'djangorestframework',
    ],
    zip_safe=False,  # Zipping prevents Django from finding migrations.
    include_package_data=True,
)
