import os
import sys
sys.path.append('/home/nacossbiu/nacoss_biu')
sys.path.append('/usr/lib/python2.7/site-packages/django')
#sys.path.append('/home/nacossbiu/.local/lib/python2.7/site-packages')
#from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'nacoss_biu.settings'
import django.core.handlers.wsgi as corestuff
print sys.path
application = corestuff.WSGIHandler()

#application = get_wsgi_application()
