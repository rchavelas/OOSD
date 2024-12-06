# Ex1_Bathtub.py
#
'''
A simple model of a bathtub
'''
from OOSD import SdModel

# Bathtub example
sdm = SdModel(name="Bathtub", start=0, end=60, dt=0.5, 
              save_step=1, time_units="minutes")

sdm.add_stock(name="bathtub", initial="initial", units="liters", 
              outflow="to_drain", inflow="from_plumbing")

sdm.add_flow(name="to_drain", equation="bathtub/delay", units="liters/minute")
sdm.add_flow(name="from_plumbing", equation="2", units="liters/minute")

sdm.add_auxiliary(name="delay", equation=2, units="minutes")
sdm.add_auxiliary(name="initial", equation=500, units="liters")

print(type(sdm))

