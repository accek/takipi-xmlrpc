##################################################
# file: takipi_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     wsdl2py takipi.wsdl
# 
##################################################

from takipi_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class takipiLocator:
    takipiSOAP_address = "http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/"
    def gettakipiSOAPAddress(self):
        return takipiLocator.takipiSOAP_address
    def gettakipiSOAP(self, url=None, **kw):
        return takipiSOAPSOAP(url or takipiLocator.takipiSOAP_address, **kw)

# Methods
class takipiSOAPSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: Tag
    def Tag(self, request, **kw):
        if isinstance(request, TA_OperationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/Tag", **kw)
        # no output wsaction
        response = self.binding.Receive(TA_OperationResponse.typecode)
        return response

    # op: Lemmatize
    def Lemmatize(self, request, **kw):
        if isinstance(request, LE_OperationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/Lemmatize", **kw)
        # no output wsaction
        response = self.binding.Receive(LE_OperationResponse.typecode)
        return response

    # op: Tokenize
    def Tokenize(self, request, **kw):
        if isinstance(request, TO_OperationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/Tokenize", **kw)
        # no output wsaction
        response = self.binding.Receive(TO_OperationResponse.typecode)
        return response

    # op: AnalyzeMorphology
    def AnalyzeMorphology(self, request, **kw):
        if isinstance(request, AN_OperationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/AnalyzeMorphology", **kw)
        # no output wsaction
        response = self.binding.Receive(AN_OperationResponse.typecode)
        return response

    # op: SplitIntoSentences
    def SplitIntoSentences(self, request, **kw):
        if isinstance(request, SP_OperationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/SplitIntoSentences", **kw)
        # no output wsaction
        response = self.binding.Receive(SP_OperationResponse.typecode)
        return response

    # op: GetStatus
    def GetStatus(self, request, **kw):
        if isinstance(request, GS_TokenRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/GetStatus", **kw)
        # no output wsaction
        response = self.binding.Receive(GS_StatusResponse.typecode)
        return response

    # op: GetResult
    def GetResult(self, request, **kw):
        if isinstance(request, GR_TokenRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/GetResult", **kw)
        # no output wsaction
        response = self.binding.Receive(GR_OperationResponse.typecode)
        return response

    # op: DeleteRequest
    def DeleteRequest(self, request, **kw):
        if isinstance(request, DR_TokenRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/DeleteRequest", **kw)
        # no output wsaction
        response = self.binding.Receive(DR_DeleteResponse.typecode)
        return response

class TA_OperationRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        text -- part text
        format -- part format
        useGuesser -- part useGuesser
        """
        self._text =  kw.get("text")
        self._format =  kw.get("format")
        self._useGuesser =  kw.get("useGuesser")
TA_OperationRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","Tag"), ofwhat=[ZSI.TC.String(pname="text", aname="_text", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ns0.DocumentFormat_Def(pname="format", aname="_format", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.Boolean(pname="useGuesser", aname="_useGuesser", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=TA_OperationRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class TA_OperationResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        TagResponse -- part TagResponse
        """
        self._TagResponse =  kw.get("TagResponse")
TA_OperationResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","TagResponse"), ofwhat=[ns0.TaggerResponse_Def(pname="TagResponse", aname="_TagResponse", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=TA_OperationResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class LE_OperationRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        text -- part text
        format -- part format
        useGuesser -- part useGuesser
        """
        self._text =  kw.get("text")
        self._format =  kw.get("format")
        self._useGuesser =  kw.get("useGuesser")
LE_OperationRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","Lemmatize"), ofwhat=[ZSI.TC.String(pname="text", aname="_text", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ns0.DocumentFormat_Def(pname="format", aname="_format", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.Boolean(pname="useGuesser", aname="_useGuesser", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=LE_OperationRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class LE_OperationResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        TagResponse -- part TagResponse
        """
        self._TagResponse =  kw.get("TagResponse")
LE_OperationResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","LemmatizeResponse"), ofwhat=[ns0.TaggerResponse_Def(pname="TagResponse", aname="_TagResponse", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=LE_OperationResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class TO_OperationRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        text -- part text
        format -- part format
        useGuesser -- part useGuesser
        """
        self._text =  kw.get("text")
        self._format =  kw.get("format")
        self._useGuesser =  kw.get("useGuesser")
TO_OperationRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","Tokenize"), ofwhat=[ZSI.TC.String(pname="text", aname="_text", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ns0.DocumentFormat_Def(pname="format", aname="_format", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.Boolean(pname="useGuesser", aname="_useGuesser", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=TO_OperationRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class TO_OperationResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        TagResponse -- part TagResponse
        """
        self._TagResponse =  kw.get("TagResponse")
TO_OperationResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","TokenizeResponse"), ofwhat=[ns0.TaggerResponse_Def(pname="TagResponse", aname="_TagResponse", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=TO_OperationResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class AN_OperationRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        text -- part text
        format -- part format
        useGuesser -- part useGuesser
        """
        self._text =  kw.get("text")
        self._format =  kw.get("format")
        self._useGuesser =  kw.get("useGuesser")
AN_OperationRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","AnalyzeMorphology"), ofwhat=[ZSI.TC.String(pname="text", aname="_text", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ns0.DocumentFormat_Def(pname="format", aname="_format", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.Boolean(pname="useGuesser", aname="_useGuesser", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=AN_OperationRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class AN_OperationResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        TagResponse -- part TagResponse
        """
        self._TagResponse =  kw.get("TagResponse")
AN_OperationResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","AnalyzeMorphologyResponse"), ofwhat=[ns0.TaggerResponse_Def(pname="TagResponse", aname="_TagResponse", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=AN_OperationResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class SP_OperationRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        text -- part text
        format -- part format
        useGuesser -- part useGuesser
        """
        self._text =  kw.get("text")
        self._format =  kw.get("format")
        self._useGuesser =  kw.get("useGuesser")
SP_OperationRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","SplitIntoSentences"), ofwhat=[ZSI.TC.String(pname="text", aname="_text", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ns0.DocumentFormat_Def(pname="format", aname="_format", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.Boolean(pname="useGuesser", aname="_useGuesser", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=SP_OperationRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class SP_OperationResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        TagResponse -- part TagResponse
        """
        self._TagResponse =  kw.get("TagResponse")
SP_OperationResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","SplitIntoSentencesResponse"), ofwhat=[ns0.TaggerResponse_Def(pname="TagResponse", aname="_TagResponse", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=SP_OperationResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class GS_TokenRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        token -- part token
        """
        self._token =  kw.get("token")
GS_TokenRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","GetStatus"), ofwhat=[ZSI.TC.String(pname="token", aname="_token", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=GS_TokenRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class GS_StatusResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        status -- part status
        """
        self._status =  kw.get("status")
GS_StatusResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","GetStatusResponse"), ofwhat=[ZSI.TCnumbers.Iint(pname="status", aname="_status", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=GS_StatusResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class GR_TokenRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        token -- part token
        """
        self._token =  kw.get("token")
GR_TokenRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","GetResult"), ofwhat=[ZSI.TC.String(pname="token", aname="_token", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=GR_TokenRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class GR_OperationResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        TagResponse -- part TagResponse
        """
        self._TagResponse =  kw.get("TagResponse")
GR_OperationResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","GetResultResponse"), ofwhat=[ns0.TaggerResponse_Def(pname="TagResponse", aname="_TagResponse", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=GR_OperationResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class DR_TokenRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        token -- part token
        """
        self._token =  kw.get("token")
DR_TokenRequest.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","DeleteRequest"), ofwhat=[ZSI.TC.String(pname="token", aname="_token", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=DR_TokenRequest, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")

class DR_DeleteResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        status -- part status
        """
        self._status =  kw.get("status")
DR_DeleteResponse.typecode = Struct(pname=("http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/","DeleteRequestResponse"), ofwhat=[ZSI.TC.Boolean(pname="status", aname="_status", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=DR_DeleteResponse, encoded="http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/")
