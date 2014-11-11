import os
import json

DOMAIN = {}


for filename in os.listdir(os.path.dirname(os.path.realpath(__file__))+'/eve/domain'):
	f = open(os.path.dirname(os.path.realpath(__file__))+'/eve/domain/'+filename)
	DOMAIN[filename.split('.json')[0]] = json.loads(f.read())

MONGO_HOST = os.environ.get('MONGO_HOST','localhost')
MONGO_PORT = os.environ.get('MONGO_PORT',27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '') 
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD','')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME','apitest')

DATE_FORMAT='%Y-%m-%dT%H:%M:%S.%fZ'
DEBUG = os.environ.get('DEBUG', False)
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
