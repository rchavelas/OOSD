from OOSD import SdModel

# Bathtub example
sdm = SdModel(name="Bathtub1", start=0, end=60, dt=0.5, 
              save_step=1, time_units="minutes")

type(SdModel)

sdm.add_stock(name = "bathtub", 
              initial = "initial",
              units = "liters",
              outflow = ["to_drain"])

sdm.add_flow(name = "to_drain",
             equation = "bathtub/delay")

sdm.add_auxiliary(name = "delay",
                  equation   = 2,
                  units = "minutes")

sdm.add_auxiliary(name = "initial",
                  equation   = 500,
                  units = "liters")

print(sdm)

# Smooth3i model
sdm3i = SdModel()