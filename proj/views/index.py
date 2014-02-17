from flask.ext.restful import Resource


class Index(Resource):

    def get(self):
        return 'hello world'
