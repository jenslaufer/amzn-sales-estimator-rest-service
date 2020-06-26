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


estimations = {
    'item_title': 'estimations',
    'schema': {
        'bestseller_rank': {
            'type': 'integer',
            'required': True
        },
        'category': {
            'type': 'string',
            'required': True
        },
        'estimated_sales': {
            'type': 'integer'
        }
    }}


DOMAIN = {
    'estimations': estimations
}
