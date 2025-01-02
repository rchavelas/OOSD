# aux_funcs.py

# Import minidom for XML handlings
import xml.dom.minidom

# Parse base XML file
base_XML_str="""
<xmile version="1.0" xmlns="http://docs.oasis-open.org/xmile/ns/XMILE/v1.0">
</xmile>
""".replace("\n", "")
base_XML=xml.dom.minidom.parseString(base_XML_str)

# Define auxiliary graphical function
def gf(name: str = None, 
       xscale: tuple[int | float, int | float] = None, 
       yscale: tuple[int | float, int | float] = None,
       xpts: list[int | float] = None, 
       ypts: list[int | float] = None,  
       units: str = None, 
       type: str = "continuous"):
    
    """Creates a graphical function.

    Note that...

    The type of graphical function define how intermediate and out-of-range
    values are calculated. Note that in the case of discrete graphical 
    functions, the last two values of the ypts list must be equal when
    building the function along with xpts, this is neded to build a last
    interval of the discrete function that makes sense. 

    * continuous: Intermediate values are calculated with linear 
    interpolation between the intermediate points. Out-of-range values
    are the same as the closest endpoint(i.e. no extrapolation is
    performed).

    * extrapolate: Intermediate values are calculated with linear
    interpolation between the intermediate points. Out-of-range
    values are calculated with linear extrapolation from the last two
    values at either end.

    * discrete: Intermediate values take on the value associated with
    the next lower x-coordinate (also called a step-wise function).
    The last two points of a discrete grahpical function must have the 
    same y value. Out-of-range values are the same as the closest
    endpoint (i.e, no extrapolation is performed).

    Args:
        name (str, optional): Name of the graphical function.
        ...
        units (str, optional): Unit of measure of the auxiliary.
        type (str) Type of graphical function, either "continuous", "extrapolate" or "discrete".
    """

    # Break if arguments are not of the required types

    # Break if ypts is not specified
    if ypts is None:
        raise Exception("ypts must always be specified")

    # Break if xscale and xpts are included at the same time
    if xscale is not None and xpts is not None:
        raise Exception("overspecified graphical function, you must only provide xscale or xpts, not both")
    
    # Break if not one xscale or xpts is included
    if xscale is None and xpts is None:
        raise Exception("underspecified graphical function, you must provide an xscale argument or an xpts argument")

    # Break if xpts (is included) and ypts are of different lengths
    if xpts is not None and ypts is not None:
        if len(xpts) != len(ypts):
            raise Exception("xpts and ypts must have the same number of elements")

    # Create gf tag
    gf_tag = base_XML.createElement("gf")

    # Append name as an attribute
    if name is not None:
        gf_tag.setAttribute("name", name)

    # Append type as attribute (must be continuous, extrapolate or discrete)
    if type in ["continuous","extrapolate","discrete"]:
        gf_tag.setAttribute("type", type)
    else:
        raise Exception('type attribute can only be "continuous", "extrapolate" or "discrete"')

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

    # Create and append xpts tag
    if xpts is not None and len(xpts)>0:
        xpts_tag = base_XML.createElement("xpts")
        xpts_tag.appendChild(base_XML.createTextNode(", ".join(map(str,xpts))))
        gf_tag.appendChild(xpts_tag)

    # Create and append ypts tag
    if ypts is not None and len(ypts)>0:
        ypts_tag = base_XML.createElement("ypts")
        ypts_tag.appendChild(base_XML.createTextNode(", ".join(map(str,ypts))))
        gf_tag.appendChild(ypts_tag) 

    # Return gf
    return gf_tag
