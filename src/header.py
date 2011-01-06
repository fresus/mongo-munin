
import urllib2
import sys
import os

DEFAULT_PORT = 28017

try:
    import json
except ImportError:
    import simplejson as json


def getServerStatus(port):
    host = os.environ.get("host", "127.0.0.1")
    raw = urllib2.urlopen( "http://%s:%d/_status" % (host, port) ).read()
    return json.loads( raw )["serverStatus"]
