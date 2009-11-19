from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging

from StringIO import StringIO
import traceback
import xmlrpclib
from xmlrpcserver import XmlRpcServer

from takipi_client import *

class Application:
    def __init__(self):
        loc = takipiLocator()
        self.port = loc.gettakipiSOAP()

    def Tag(self, meta, text, format, useGuesser):
        """Submit a text for processing. Split the text into sentences and
        tokens, get a set of possible morphological analysis for every token
        and disambiguate it.

        Arguments:
          text: Text to process.
          format: Format of the text (TXT, PLAIN or CORPUS).
          useGuesser: Indicates whether use the Guesser module.

        Returns:
          status dictionary with keys 'status' and 'msg'
        """

        req = TA_OperationRequest(text=text, format=format, useGuesser=useGuesser)
        rsp = self.port.Tag(req)._TagResponse
        return rsp._attrs

    def Lemmatize(self, meta, text, format, useGuesser):
        """Submit a text for processing. Every token in the text will be
        substitute with its lemma.

        Arguments:
          text: Text to process.
          format: Format of the text (TXT, PLAIN or CORPUS).
          useGuesser: Indicates whether use the Guesser module.

        Returns:
          status dictionary with keys 'status' and 'msg'
        """

        req = LE_OperationRequest(text=text, format=format, useGuesser=useGuesser)
        rsp = self.port.Lemmatize(req)._TagResponse
        return rsp._attrs

    def Tokenize(self, meta, text, format, useGuesser):
        """Submit text for processing. Split the text into tokens.

        Arguments:
          text: Text to process.
          format: Format of the text (TXT, PLAIN or CORPUS).
          useGuesser: Indicates whether use the Guesser module (ignored).

        Returns:
          status dictionary with keys 'status' and 'msg'
        """

        req = TO_OperationRequest(text=text, format=format, useGuesser=useGuesser)
        rsp = self.port.Tokenize(req)._TagResponse
        return rsp._attrs

    def AnalyzeMorphology(self, meta, text, format, useGuesser):
        """Submit a text for processing. Split the text into sentences and
        tokens. Get a set of possible morphological analysis for every token.

        Arguments:
          text: Text to process.
          format: Format of the text (TXT, PLAIN or CORPUS).
          useGuesser: Indicates whether use the Guesser module (ignored).

        Returns:
          status dictionary with keys 'status' and 'msg'
        """

        req = AN_OperationRequest(text=text, format=format, useGuesser=useGuesser)
        rsp = self.port.AnalyzeMorphology(req)._TagResponse
        return rsp._attrs

    def SplitIntoSentences(self, meta, text, format, useGuesser):
        """Submit a text for processing. Split the text into sentences.

        Arguments:
          text: Text to process.
          format: Format of the text (TXT, PLAIN or CORPUS).
          useGuesser: Indicates whether use the Guesser module (ignored).

        Returns:
          status dictionary with keys 'status' and 'msg'
        """

        req = SP_OperationRequest(text=text, format=format, useGuesser=useGuesser)
        rsp = self.port.SplitIntoSentences(req)._TagResponse
        return rsp._attrs

    def GetStatus(self, meta, token):
        """Get the results for a request identified by a given token.

        Arguments:
          token: request token

        Returns:
          int, status code
        """

        req = GS_TokenRequest(token=token)
        rsp = self.port.GetStatus(req)
        return rsp

    def GetResult(self, meta, token):
        """Get the results for a request identified by a given token.

        Arguments:
          token: request token

        Returns:
          status dictionary with keys 'status' and 'msg'
        """

        req = GR_TokenRequest(token=token)
        rsp = self.port.GetResult(req)._TagResponse
        return rsp._attrs

    def DeleteRequest(self, meta, token):
        """Delete the request from the database.

        Arguments:
          token: request token

        Returns:
          1 if successful, 0 otherwise
        """

        req = DR_TokenRequest(token=token)
        rsp = self.port.DeleteRequest(req)
        return int(rsp)


class XMLRpcHandler(webapp.RequestHandler):
    rpcserver = None

    def __init__(self):
        self.rpcserver = XmlRpcServer()
        app = Application()
        self.rpcserver.register_class('takipi', app)

    def post(self):
        request = StringIO(self.request.body)
        request.seek(0)
        response = StringIO()
        try:
            self.rpcserver.execute(request, response, None)
        except Exception, e:
            logging.error('Error executing: '+str(e))
            for line in traceback.format_exc().split('\n'):
                logging.error(line)
        finally:
            response.seek(0)

        rstr = response.read()
        self.response.headers['Content-type'] = 'text/xml'
        self.response.headers['Content-length'] = "%d" % len(rstr)
        self.response.out.write(rstr)

application = webapp.WSGIApplication([('/xmlrpc/', XMLRpcHandler)],
        debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
    main()

