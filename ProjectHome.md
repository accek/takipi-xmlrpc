EU CLARIN project provides [SOAP-based access to Polish Language Tagger TaKIPI](http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/). This project aims at providing simpler XML-RPC based interface to the same infrastructure.

Included is a Google App Engine based proxy server which translates XML-RPC messages to SOAP and back.

A working installation can be accessed via XML-RPC at http://takipi-xmlrpc.appspot.com/xmlrpc/ (please note the trailing slash).

## How to use ##

Feel free to experiment with provided [xmlrpc-client.py](http://takipi-xmlrpc.googlecode.com/svn/trunk/xmlrpc-client.py)

Example:

```
$ echo "W wielkim lesie po kryjomu wielka mucha szła do domu." | ./xmlrpc-client.py Lemmatize
TOKEN=473:356bb514d6ec0d7e1568a3f8d1549b8ed96e3f3b7005a6a5f02b6e815d997f5b
w wielki las po kryjom wielki mucha iść do dom .
```

Refer to original [TaKIPI-WS Documentation](http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/clarin_takipi_ws_v0.4.pdf) for information about available commands.

You can also use standard `system.listMethods` and `system.methodHelp` introspection factilities with XML-RPC.