from re import match
from sys import exit
from socket import inet_aton

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

app_name = '{{cookiecutter.app_name}}'
sanic_host = '{{cookiecutter.sanic_host}}'

if not match(MODULE_REGEX, app_name):
    print('ERROR: App Name {} is not a valid Python Module.'
          'Please use _ instead of - in App Name'.format(app_name))
    exit(1)

try:
    inet_aton(sanic_host)
except:
    print('ERROR: Invalid Sanic App Host {}'.format(sanic_host))
