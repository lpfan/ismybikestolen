from proj import api
from views import index

api.add_resource(index.Index, '/index')



