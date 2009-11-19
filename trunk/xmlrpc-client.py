#!/usr/bin/env python

# Usage: xmlrpc-client.py operation < text

import xmlrpclib, time, sys

s = xmlrpclib.Server('http://localhost:8080/xmlrpc/')
#s = xmlrpclib.Server('http://takipi-xmlrpc.appspot.com/xmlrpc/')

op = sys.argv[1]
cmd = getattr(s.takipi, op)
resp = cmd(sys.stdin.read(), "TXT", True)
token = resp['msg']
print >>sys.stderr, "TOKEN=%s" % token

while resp['status'] in (2, 3):
    time.sleep(1)
    resp = s.takipi.GetResult(token)

if resp['status'] == 1:
    print resp['msg']
else:
    sys.exit(1)
