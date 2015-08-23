"""
WSGI config for SecurityTrainingGround project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys


# These two lines are only necessary if your default python isn't python3
# Make sure INTERP points to the python3 you want to run...
#INTERP = os.path.expanduser("~/opt/python-3.4.3/bin/python")
#if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)


sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "/SecurityTrainingGround")
os.environ["DJANGO_SETTINGS_MODULE"] = "SecurityTrainingGround.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
