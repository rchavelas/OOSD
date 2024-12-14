# 'Object Oriented' Systems Dynamics (OOSD) model builder in python

A python package to build Systems Dynamics models as instances of the **SdModel()** class, which includes methods to add elements to the model (an thus the Object-Oriented nature of the model building process). 

One of the main goals of this package is to allow for quick prototyping of Systems Dynamics models "on the go". This prototypes can be easily grown as the project moves from simpler assumptions to more complex structures, parameters, equations and relationships. The idea behing this packages it to build XMILE models that adhere to the  4 practical reasons outlined by Eberlein and Chichakly (2013) for creating the standard: archiving, replicability, analysis and specialized tool development.

The SdModel implements methods to create comprehensive Systems Dynamics models complying with the OASIS XMILE [xmile-v1.0] open standard for System Dynamics such as:
* Stocks
* Flows 
* Auxiliaries
* Some graphical functions
* Unit integration

Currently, it doesn't support other, more advanced funtionalities such as:
* Groups
* Builtin Functions
* Submodels
* Arrays
* Styles

## References
* Eberlein, R. L. & Chichakly, K. J. (2013). XMILE: a new standard for system dynamics. *System Dynamics Review*, 29(3):188-195. https://doi.org/10.1002/sdr.1504
* [xmile-v1.0] XML Interchange Language for System Dynamics (XMILE) Version 1.0. Edited by Karim Chichakly, Gary Baxter, Robert Eberlein, Will Glass-Husain, Robert Powers, and William Schoenberg. 14 December 2015. OASIS Standard. http://docs.oasis-open.org/xmile/xmile/v1.0/os/xmile-v1.0-os.html. Latest version: http://docs.oasis-open.org/xmile/xmile/v1.0/xmile-v1.0.html.
