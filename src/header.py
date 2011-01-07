
import urllib2
import sys
import os
import re

DEFAULT_PORT = 28017

try:
    import json
except ImportError:
    import simplejson as json


def getServerPort():
    me = sys.argv[0]
    match = re.compile('.*_([0-9]+)$')
    try:
        return int(match.findall(me)[0])
    except (IndexError, ValueError):
        return DEFAULT_PORT
    
def getServerStatus():
    port = getServerPort()
    host = os.environ.get("host", "127.0.0.1")
    raw = urllib2.urlopen( "http://%s:%d/_status" % (host, port) ).read()
    return json.loads( raw )["serverStatus"]
