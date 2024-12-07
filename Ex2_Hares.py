# Ex2_Hares.py

'''
A population model of hares births and deaths from the original 
XMILE standard
'''

from OOSD import SdModel
from OOSD import gf

# Hares example
sdm_hrs = SdModel(name="Hares")

# STOCKS
sdm_hrs.add_stock(name="Hares", eqn=5E4, 
                  inflow="hare_births", outflow="hare_deaths")
sdm_hrs.add_stock(name="Lynx", eqn=1250)

# FLOWS
sdm_hrs.add_flow(name="hare_births", eqn="Hares*hare_birth_fraction")
sdm_hrs.add_flow(name="hare_deaths", eqn="Lynx*hares_killed_per_lynx")

# AUX Variables
sdm_hrs.add_auxiliary(name="hare_birth\nfraction",eqn=1.25)
sdm_hrs.add_auxiliary(name="hare\ndensity",eqn="Hares/area")
sdm_hrs.add_auxiliary(name="area",eqn=1E3)

# AUX Variables with graphical function
hares_killed_per_lynx_gf = gf.linear(xmin=0, xmax=500, 
                                     ymin=0, ymax=1000,
                                     ypts=[0,50,100,150,200,250,300,350,400,450,500])
sdm_hrs.add_auxiliary(name="hares_killed\nper_lynx", eqn="hare_density",
                      gf=hares_killed_per_lynx_gf)

