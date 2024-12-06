# Exn_Smooth31.py
#
'''
A simple model of a exponential smooth growth
'''
from OOSD import SdModel

# Smooth3i example
sdm3i = SdModel(name="Smooth3i", start=0, end=60, dt=0.5)

sdm3i.add_auxiliary(name="initial", equation=500)
sdm3i.add_auxiliary(name="input", equation=50)
sdm3i.add_auxiliary(name="delay", equation=5, units="time")

sdm3i.add_stock(name="level1", initial="initial", biflow="change_in_1")
sdm3i.add_stock(name="level2", initial="initial", biflow="change_in_2")
sdm3i.add_stock(name="smooth3i", initial="initial", biflow="change_in_3")

sdm3i.add_flow(name="change_in_1", equation="(input-level1)/delay")
sdm3i.add_flow(name="change_in_2", equation="(level1-level2)/delay")
sdm3i.add_flow(name="change_in_3", equation="(level2-smooth3i)/delay")