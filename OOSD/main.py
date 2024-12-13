# Import Minidome for XML handlings
import xml.dom.minidom

# Define base XMILE XML structure
base_XML_str="""
<xmile version="1.0" xmlns="http://docs.oasis-open.org/xmile/ns/XMILE/v1.0">
<header>
</header>
<sim_specs>
</sim_specs>
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
                 method="Euler", time_units=None):
        self.XML_rep = xml.dom.minidom.parseString(base_XML_str)

        # Create name tag and append it to header
        name_tag = base_XML.createElement("name")
        name_tag.appendChild(base_XML.createTextNode(name))
        self.XML_rep.getElementsByTagName("header")[0].appendChild(name_tag)

        # Create and append sim_specs elements
        sim_specs = self.XML_rep.getElementsByTagName("sim_specs")[0]
        ## Method and time_units attributes
        sim_specs.setAttribute("method", method)
        if time_units is not None:
            sim_specs.setAttribute("time_units", time_units)
        ## Start, stop and dt tags
        if start is not None:
            start_tag = base_XML.createElement("start")
            start_tag.appendChild(base_XML.createTextNode(str(start)))
            sim_specs.appendChild(start_tag)
        if stop is not None:
            stop_tag = base_XML.createElement("stop")
            stop_tag.appendChild(base_XML.createTextNode(str(stop)))
            sim_specs.appendChild(stop_tag)
        if dt is not None:
            dt_tag = base_XML.createElement("dt")
            dt_tag.appendChild(base_XML.createTextNode(str(dt)))
            sim_specs.appendChild(dt_tag)

    def add_stock(self, name, eqn=None,  
                  inflow=None, outflow=None):
        # Create stock tag
        stock_tag = base_XML.createElement("stock")
        stock_tag.setAttribute("name", name)
        
        # Create and append eqn tag
        if eqn is not None and isinstance(eqn, str):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(eqn))
            stock_tag.appendChild(eqn_tag)
        elif eqn is not None and (isinstance(eqn, int) or isinstance(eqn, float)):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(str(eqn)))
            stock_tag.appendChild(eqn_tag)
        #else eqn: (raise not supported type)

        # Create and append inflow tag
        if inflow is not None and isinstance(inflow, list):
            for elem in inflow:
                inflow_tag = base_XML.createElement("inflow")
                inflow_tag.appendChild(base_XML.createTextNode(elem))
                stock_tag.appendChild(inflow_tag)
        elif inflow is not None and isinstance(inflow, str):
            inflow_tag = base_XML.createElement("inflow")
            inflow_tag.appendChild(base_XML.createTextNode(inflow))
            stock_tag.appendChild(inflow_tag)
        #else inflow: (raise not supported type)

        # Create and append outflow tag
        if outflow is not None and isinstance(outflow, list):
            for elem in outflow:
                outflow_tag = base_XML.createElement("outflow")
                outflow_tag.appendChild(base_XML.createTextNode(elem))
                stock_tag.appendChild(outflow_tag)
        elif outflow is not None and isinstance(outflow, str):
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
        if eqn is not None and isinstance(eqn, str):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(eqn))
            flow_tag.appendChild(eqn_tag)
        elif eqn is not None and (isinstance(eqn, int) or isinstance(eqn, float)):
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
        if eqn is not None and isinstance(eqn, str):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(eqn))
            aux_tag.appendChild(eqn_tag)
        elif eqn is not None and (isinstance(eqn, int) or isinstance(eqn, float)):
            eqn_tag = base_XML.createElement("eqn")
            eqn_tag.appendChild(base_XML.createTextNode(str(eqn)))
            aux_tag.appendChild(eqn_tag)
        #else eqn: (raise not supported type)

        # Append aux to model
        model = self.XML_rep.getElementsByTagName("model")[0]
        model.appendChild(aux_tag)

    def __str__(self):
        return self.XML_rep.toprettyxml()
