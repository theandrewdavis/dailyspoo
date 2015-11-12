#!/usr/bin/env python3

import bottle
import datetime
import os
import pytz

@bottle.route('/')
def index():
    images = os.listdir('spoos')
    utc = pytz.timezone('UTC')
    eastern = pytz.timezone('US/Eastern')
    now = utc.localize(datetime.datetime.utcnow()).astimezone(eastern)
    epoch = eastern.localize(datetime.datetime(1970, 1, 1))
    index = (now - epoch).days % len(images)
    return bottle.template('index.html', img=os.path.join('spoos', images[index]))

@bottle.route('/spoos/<filename>')
def static(filename):
    print('Serving {}'.format(filename))
    return bottle.static_file(filename, root='spoos')

bottle.run(host='localhost', port=8080)
