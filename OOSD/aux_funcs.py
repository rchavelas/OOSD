# aux_funcs.py

# Import minidom for XML handlings
import xml.dom.minidom

# Parse base XML file
base_XML_str="""
<xmile version="1.0" xmlns="http://docs.oasis-open.org/xmile/ns/XMILE/v1.0">
</xmile>
""".replace("\n", "")
base_XML=xml.dom.minidom.parseString(base_XML_str)

# Define graphical function auxiliary function
def gf(name: str, 
       xscale: tuple[int | float, int | float] = None, 
       yscale: tuple[int | float, int | float] = None,
       xpts: list[int | float] = None, 
       ypts: list[int | float] = None,  
       units: str = None, type: str = "continuous"):
    
    """Creates a graphical function.

    Note that...

    Args:
        name (str): Name of the continous graphical function.
        ...
        units (str): Unit of measure of the auxiliary.
    """

    # Break if arguments are not of the required types

    # Break if xscale and xpts are included at the same time
    if xscale is not None and xpts is not None:
        raise Exception("overspecified graphical function, you must only provide xscale or xpts, not both")
    
    # Break if not one xscale or xpts is included

    # Create gf tag
    gf_tag = base_XML.createElement("gf")
    gf_tag.setAttribute("name", name)
    gf_tag.setAttribute("type", type)

    # Create and append xscale tag
    if xscale is not None and len(xscale) == 2:
        xscale_tag = base_XML.createElement("xscale")
        xscale_tag.setAttribute("min", str(xscale[0]))
        xscale_tag.setAttribute("max", str(xscale[1]))
        gf_tag.appendChild(xscale_tag)

    # Create and append yscale tag
    if yscale is not None and len(yscale) == 2:
        yscale_tag = base_XML.createElement("yscale")
        yscale_tag.setAttribute("min", str(yscale[0]))
        yscale_tag.setAttribute("max", str(yscale[1]))
        gf_tag.appendChild(yscale_tag)

    # Create and append ypts tag
    if ypts is not None and len(ypts)>0:
        ypts_tag = base_XML.createElement("ypts")
        ypts_tag.appendChild(base_XML.createTextNode(", ".join(map(str,ypts))))
        gf_tag.appendChild(ypts_tag) 

    # Return gf
    return gf_tag
