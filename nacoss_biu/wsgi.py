"""
WSGI config for nacoss_biu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/nacossbiu/nacoss_biu')
sys.path.append('/home/nacossbiu/.local/lib/python2.7/site-packages')
#os.environ.setdefault("PYTHON_EGG_CACHE", "/tmp")

#print sys.path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nacoss_biu.settings")

application = get_wsgi_application()
