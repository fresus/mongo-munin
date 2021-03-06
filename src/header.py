
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
    url = "http://%s:%d/_status" % (host, port)
    req = urllib2.Request(url)
    user = os.environ.get("user")
    password = os.environ.get("password")
    if user and password:
        passwdmngr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passwdmngr.add_password(None, 'http://%s:%d' % (host, port), user, password)
        authhandler = urllib2.HTTPDigestAuthHandler(passwdmngr)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
    raw = urllib2.urlopen(req).read()
    return json.loads( raw )["serverStatus"]
