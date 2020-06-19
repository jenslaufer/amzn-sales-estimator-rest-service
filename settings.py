# -*- coding: utf-8 -*-

import os
import pymongo

MONGO_URI = os.environ.get(
    'MONGODB_URI', 'mongodb://localhost/fiverr')


RESOURCE_METHODS = ['GET', 'POST']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

X_DOMAINS = '*'
X_HEADERS = 'Content-Type,Authorization'


predictions = {
    'item_title': 'suggestions',
    'schema': {
        'bsr': {
            'type': 'int',
            'required': True
        },

        'sales': {
            'type': 'int'
        }
    }}


DOMAIN = {
    'predictions': predictions
}
