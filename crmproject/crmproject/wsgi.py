
import os
import sys
import site
envpath = '/var/crm_env/lib/python3.6/site-packages'
site.addsitedir(envpath)
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),".")))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crmproject.settings')

application = get_wsgi_application()
