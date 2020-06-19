import os
from eve import Eve
import logging

loglevel = int(os.environ.get('LOGLEVEL', 10))
logging.basicConfig(level=loglevel)

app = Eve()
host = os.environ.get('HOST', '0.0.0.0')

if __name__ == "__main__":
    app.run(host=host)
