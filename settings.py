# -*- coding: utf-8 -*-

import os
import pymongo

MONGO_URI = os.environ.get("MONGO_URI", 'mongodb://localhost/prediction')


RESOURCE_METHODS = ['GET', 'POST']

ITEM_METHODS = ['GET', 'DELETE']

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
