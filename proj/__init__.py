#coding: utf-8

'''
    * Date: 14.02.14
    * Author: mishashchetinin
'''

from flask import Flask
from flask.ext import restful


app = Flask(__name__)
api = restful.Api(app)

import routers



