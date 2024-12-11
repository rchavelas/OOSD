# Import Minidome for XML handlings
import xml.dom.minidom

# Define base XMILE XML structure
base_XML_str="""
<xmile version="1.0" xmlns="http://docs.oasis-open.org/xmile/ns/XMILE/v1.0">
<header>
</header>
<model>
</model>
</xmile>
""".replace("\n", "")

# Read base XML file
base_XML=xml.dom.minidom.parseString(base_XML_str)

class SdModel:
    ''' 
    This class helps build Systems Dynamics models in Python 
    
    It complies with the XMILE standard

    '''

    def __init__(self, name, start=None, stop=None, dt=None, 
                 save_step=None, time_units=None):
        self.name = name
        self.start = start
        self.stop = stop
        self.dt = dt
        self.time_units = time_units
        self.XML_rep = xml.dom.minidom.parseString(base_XML_str)

    def add_stock(self, name, eqn=None,  
                  inflow=None, outflow=None):
        # Create stock tag
        stock_tag = base_XML.createElement("stock")
        stock_tag.setAttribute("name", name)
        
        # Create and append eqn tag
        if eqn and isinstance(eqn, str):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(eqn))
            stock_tag.appendChild(eqn_tag)
        elif eqn and (isinstance(eqn, int) or isinstance(eqn, float)):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(str(eqn)))
            stock_tag.appendChild(eqn_tag)
        #else eqn: (raise not supported type)

        # Create and append inflow tag
        if inflow and isinstance(inflow, list):
            for elem in inflow:
                inflow_tag = base_XML.createElement("inflow")
                inflow_tag.appendChild(base_XML.createTextNode(elem))
                stock_tag.appendChild(inflow_tag)
        elif inflow and isinstance(inflow, str):
            inflow_tag = base_XML.createElement("inflow")
            inflow_tag.appendChild(base_XML.createTextNode(inflow))
            stock_tag.appendChild(inflow_tag)
        #else inflow: (raise not supported type)

        # Create and append outflow tag
        if outflow and isinstance(outflow, list):
            for elem in outflow:
                outflow_tag = base_XML.createElement("outflow")
                outflow_tag.appendChild(base_XML.createTextNode(elem))
                stock_tag.appendChild(outflow_tag)
        elif inflow and isinstance(outflow, str):
            outflow_tag = base_XML.createElement("outflow")
            outflow_tag.appendChild(base_XML.createTextNode(outflow))
            stock_tag.appendChild(outflow_tag)
        #else outflow: (raise not supported type)

        # Append stock to model
        model = self.XML_rep.getElementsByTagName("model")[0]
        model.appendChild(stock_tag)


    def add_flow(self, name, eqn=None):
        # Create flow tag
        flow_tag = base_XML.createElement("flow")
        flow_tag.setAttribute("name", name)

        # Create and append eqn tag
        if eqn and isinstance(eqn, str):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(eqn))
            flow_tag.appendChild(eqn_tag)
        elif eqn and (isinstance(eqn, int) or isinstance(eqn, float)):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(str(eqn)))
            flow_tag.appendChild(eqn_tag)
        #else eqn: (raise not supported type)

        # Append flow to model
        model = self.XML_rep.getElementsByTagName("model")[0]
        model.appendChild(flow_tag)

    def add_auxiliary(self, name, eqn=None):
        # Create aux tag
        aux_tag = base_XML.createElement("aux")
        aux_tag.setAttribute("name", name)

        # Create and append eqn tag
        if eqn and isinstance(eqn, str):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(eqn))
            aux_tag.appendChild(eqn_tag)
        elif eqn and (isinstance(eqn, int) or isinstance(eqn, float)):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(str(eqn)))
            aux_tag.appendChild(eqn_tag)
        #else eqn: (raise not supported type)

        # Append aux to model
        model = self.XML_rep.getElementsByTagName("model")[0]
        model.appendChild(aux_tag)

    def __str__(self):
        return self.XML_rep.toprettyxml()
