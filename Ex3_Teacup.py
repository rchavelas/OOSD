"""Example 3: Original Teacup model from the PYSD tutorial"""
from OOSD import SdModel

sdm = SdModel(name="Teacup", start=0, stop=30.0, dt=0.125)

# Add stocks to main model
sdm.add_stock(name="Teacup_temperature", 
              doc="The average temperature of the tea and the cup",
              eqn="180", outflow="Heat_Loss_to_Room")

# Add flows to main model
sdm.add_flow(name="Heat_loss_to_room", 
             doc="Heat loss to room",
             eqn="(Teacup_temperature - Room_temperature) / Characteristic_time")

# Add auxiliaries to main model
sdm.add_auxiliary(name="Characteristic_time", eqn=10)
sdm.add_auxiliary(name="Room_temperature", eqn=70,
                  doc="Ambient Room Temperature")  

sdm.save_xmile()