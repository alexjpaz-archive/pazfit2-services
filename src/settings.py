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

IF_MATCH= os.environ.get('IF_MATCH', True)

X_DOMAINS='*'
X_HEADERS='Accept, Cache-Control, Pragma, Origin, Authorization, Content-Type, X-Requested-With, Etag'
X_EXPOSE_HEADERS='Cache-Control, Content-Language, Content-Type, Expires, Last-Modified, Pragma, Etag'

DATE_FORMAT='%Y-%m-%dT%H:%M:%S.%fZ'
DEBUG = os.environ.get('DEBUG', False)
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
