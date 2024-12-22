"""Example 4: Practitioners example from  XMILE V1.0 examples"""
from OOSD import SdModel

sdm = SdModel(name="Ex4_Practitioners", start=0, stop=12, dt=0.25,
              method="Euler", time_units="Year")

sdm.add_stock(name="Practitioners", 
              eqn=100,
              inflow="Adopting",
              units="Person")

sdm.add_flow(name="Adopting",
             eqn="Practitioners * Adoption_rate",
             units="Person/Year")

sdm.add_auxiliary(name="Adoption_rate",
                  eqn=0.03,
                  units="1/Year")

sdm.save_xmile()

'''
sdm = SdModel(name="Teacup", start=0, stop=30.0, dt=0.125)

# Add stocks to main model
sdm.add_stock(name="Teacup_temperature", 
              doc="The average temperature of the tea and the cup",
              eqn="180", 
              outflow="Heat_Loss_to_Room")  

# Add flows to main model
sdm.add_flow(name="Heat_loss_to_room", 
             doc="Heat loss to room",
             eqn="(Teacup_temperature - Room_temperature) / Characteristic_time")

# Add auxiliaries to main model
sdm.add_auxiliary(name="Characteristic_time", 
                  eqn=10)
sdm.add_auxiliary(name="Room_temperature", 
                  eqn=70,
                  doc="Ambient Room Temperature")  

sdm.save_xmile()
'''
