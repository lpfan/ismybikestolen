#coding: utf-8

'''
    * Date: 14.02.14
    * Author: mishashchetinin
'''

from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True

import route



