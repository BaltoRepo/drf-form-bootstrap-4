#!/bin/bash
set -x
set -e
# Coverage runs the file we tell it to (it doesn't use the search path from our shell), and our settings
# are in the root, so we must put django-admin.py in the root.
cp $(which django-admin.py) django-admin.py
PYTHONPATH=$(pwd) coverage run --source drfformbootstrap4 django-admin.py test . --settings=test_settings
rm django-admin.py
coverage report -m
