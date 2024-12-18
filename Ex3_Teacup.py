"""Example 3: Original Teacup model from the PYSD tutorial"""
from OOSD import SdModel

sdm = SdModel(name="Teacup", start=0, stop=30.0, dt=1)

# Add stocks to main model
sdm.add_stock(name="Teacup_Temperature", 
              doc="The average temperature of the tea and the cup",
              eqn="180", outflow="Heat_Loss_to_Room")

# Add flows to main model
sdm.add_flow(name="Heat_Loss_to_Room", 
             doc="Heat Loss to Room",
             eqn="(Teacup_Temperature - Room_Temperature) / Characteristic_Time")

# Add auxiliaries to main model
sdm.add_auxiliary(name="Characteristic_Time", eqn=10)
sdm.add_auxiliary(name="Room_Temperature", eqn=70,
                  doc="Ambient Room Temperature")  

sdm.save_xmile()