
name = "connections"


def doData():
    print name + ".value " + str( getServerStatus()["connections"]["current"] )

def doConfig():

    print "graph_title MongoDB current connections (%s)" % (getServerPort())
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel connections"
    print "graph_category MongoDB"

    print name + ".label " + name





