# Exn_Smooth31.py
#
'''
A simple model of a exponential smooth growth
'''
from OOSD import SdModel

# Smooth3i example
sdm3i = SdModel(name="Smooth3i", start=0, stop=60, dt=0.5)

sdm3i.add_auxiliary(name="initial", eqn=500)
sdm3i.add_auxiliary(name="input", eqn=50)
sdm3i.add_auxiliary(name="delay", eqn=5, units="time")

sdm3i.add_stock(name="level1", eqn="initial", biflow="change_in_1")
sdm3i.add_stock(name="level2", eqn="initial", biflow="change_in_2")
sdm3i.add_stock(name="smooth3i", eqn="initial", biflow="change_in_3")

sdm3i.add_flow(name="change_in_1", eqn="(input-level1)/delay")
sdm3i.add_flow(name="change_in_2", eqn="(level1-level2)/delay")
sdm3i.add_flow(name="change_in_3", eqn="(level2-smooth3i)/delay")