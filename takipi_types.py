##################################################
# file: takipi_types.py
#
# schema types generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#    wsdl2py takipi.wsdl
#
##################################################

import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/
##############################

class ns0:
    targetNamespace = "http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/"

    class TaggerResponse_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/"
        type = (schema, "TaggerResponse")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.TaggerResponse_Def.schema
            TClist = []
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            else:
                # attribute handling code
                self.attribute_typecode_dict["status"] = ZSI.TCnumbers.Iint()
                self.attribute_typecode_dict["msg"] = ZSI.TC.String()
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    return
            Holder.__name__ = "TaggerResponse_Holder"
            self.pyclass = Holder

    class DocumentEncoding_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/"
        type = (schema, "DocumentEncoding")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class DocumentFormat_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/"
        type = (schema, "DocumentFormat")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

# end class ns0 (tns: http://plwordnet.pwr.wroc.pl/clarin/ws/takipi/)
