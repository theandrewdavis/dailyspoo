#!/usr/bin/env python3

import bottle
import datetime
import json
import os
import pytz
import random


# Preserve order of shuffled spoo images by saving them to a file
try:
    images = json.loads(open('order.json').read())
except FileNotFoundError:
    images = os.listdir('spoos')
    random.shuffle(images)
    open('order.json', 'w').write(json.dumps(images))


@bottle.route('/')
def index():
    """Serve one spoo image a day, making sure the day is determined using EST"""
    utc = pytz.timezone('UTC')
    eastern = pytz.timezone('US/Eastern')
    now = utc.localize(datetime.datetime.utcnow()).astimezone(eastern)
    epoch = eastern.localize(datetime.datetime(1970, 1, 1))
    index = (now - epoch).days % len(images)
    return bottle.template('index.html', img=os.path.join('spoos', images[index]))

bottle.run(host='0.0.0.0', port=8001, server='cherrypy')
