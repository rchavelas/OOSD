"""Example 3: Original Teacup model from the PYSD tutorial"""
from OOSD import SdModel

sdm = SdModel(name="Teacup", start=0, stop=30.0, dt=0.125)

# Add stocks to main model
#sdm.add_stock(name="Teacup Temperature", eqn="180", outflow="'Heat Loss to Room'")
sdm.add_stock(name="Teacup_Temperature", eqn="180", outflow="Heat_Loss_to_Room")

# Add flows to main model
#sdm.add_flow(name="Heat Loss to Room", 
#             eqn="('Teacup Temperature'-'Room Temperature')/'Characteristic Time'")
sdm.add_flow(name="Heat_Loss_to_Room", 
             eqn="(Teacup_Temperature - Room_Temperature) / Characteristic_Time")

# Add auxiliaries to main model
#sdm.add_auxiliary(name="Characteristic Time", eqn=10)
#sdm.add_auxiliary(name="Room Temperature", eqn=70)  
sdm.add_auxiliary(name="Characteristic_Time", eqn=10)
sdm.add_auxiliary(name="Room_Temperature", eqn=70)  

print(sdm)