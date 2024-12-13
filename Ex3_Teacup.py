"""Teacup model PYSD"""
from OOSD import SdModel

sdm = SdModel(name="Teacup", start="", stop="", dt="")

sdm.add_stock("Teacup Temperature", eqn="", outflow="Heat Loss to Room")

sdm.add_flow(name="Heat Loss to Room", eqn="")

sdm.add_auxiliary(name="Characteristic Time", eqn="")
sdm.add_auxiliary(name="Room Temperature", eqn="")

print(sdm)