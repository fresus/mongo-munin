
name = "connections"


def doData(port):
    print name + ".value " + str( getServerStatus(port)["connections"]["current"] )

def doConfig():

    print "graph_title MongoDB current connections"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel connections"
    print "graph_category MongoDB"

    print name + ".label " + name





