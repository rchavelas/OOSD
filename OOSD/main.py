"""
This module implements a class (SdModel) to build Systems Dynamics 
models that comply with the  [xmile-v1.0] open standard. The class 
is meant to simplify the creation of Systems Dynamics models encapsulating
the requirements of the XMILE standard into a class with easy to use
methods (thus, in an object-oriented way).

TODO:
    - double-check first three methods

References:
    XML Interchange Language for System Dynamics (XMILE) Version 1.0. 
    Edited by Karim Chichakly, Gary Baxter, Robert Eberlein, Will 
    Glass-Husain, Robert Powers, and William Schoenberg. 14 December 
    2015. OASIS Standard. http://docs.oasis-open.org/xmile/xmile/v1.0/os/xmile-v1.0-os.html. 
    Latest version: http://docs.oasis-open.org/xmile/xmile/v1.0/xmile-v1.0.html.
"""

# Import minidom for XML handlings
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
    """ A class to build XMILE Compliant Systems Dynamics models in Python 
    """

    def __init__(self, name: str, start: int | float = None,
                stop: int | float = None, dt: int | float = None, 
                 method: str = "Euler", time_units: str = None) -> None:
        """Create an instance of the SdModel class.
        
        To build a Systems Dynamics model compliant with the XMILE 
        standard a ``name`` is REQUIRED. The ``start``, ``stop`` and ``dt`` 
        arguments are also required for the simulation to run.

        Args:
            name (str): Name of the whole model.
            start (int | float, optional): Start time of the simulation.
            stop (int | float, optional): Stop time of the simulation.
            dt (int | float, optional): delta time of the simulation.
            method (str, optional): integration method of the simulation.
            time_units (str, optional): time units of the whole model.
        """
        # Break if arguments are not of the required classes

        self.XML_rep = xml.dom.minidom.parseString(base_XML_str)
        """This attribute holds the XML representation of the whole model """

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

    def add_stock(self, name: str, eqn: str | int | float = None,  
                  inflow: str | list[str] = None, 
                  outflow: str | list[str] = None):
        """Append a stock to the whole model in the SdModel class.

        Note that the ``equation`` can be a string, an integer or a float,
        as any of this can describe the initial value of the stock.

        Note that the ``inflow`` and ``outflow`` arguments accept both 
        a string and a list of string, as multiple inflows and outflows 
        can interact with a given stock.

        Args:
            name (str): Name of the stock.
            eqn (str | int | float, optional): Initial value of the stock.
            inflow (str | list[str], optional): Inflow or inflows of the stock.
            outflow (str | list[str], optional): Outflow or outflows of the stock.
        """
        # Break if arguments are not of the required classes

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

    def add_flow(self, name: str, eqn: str | int | float = None):
        """Append a flow to the whole model in the SdModel class.

        Note that the ``equation`` can be a string, an integer or a float,
        as any of this can describe the behavior of the flow.

        Args:
            name (str): Name of the flow.
            eqn (str | int | float, optional): Equation of the flow.
        """
        # Break if arguments are not of the required classes

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

    def add_auxiliary(self, name: str, eqn: str | int | float = None):
        """Append an auxiliary to the whole model in the SdModel class.

        Note that the ``equation`` can be a string, an integer or a float,
        as any of this can describe the behavior of the auxiliary.

        Args:
            name (str): Name of the auxiliary.
            eqn (str | int | float, optional): Equation of the auxiliary.
        """
        # Break if arguments are not of the required classes

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

    def __str__(self) -> str:
        return self.XML_rep.toprettyxml()
