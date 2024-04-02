import pypsa
import pandas as pd
import matplotlib.pyplot as plt

network = pypsa.Network()


# add low voltage buses
for i in range(0,3):
    network.add("Bus", f"Bus{i}", v_nom = 11)

network.add("Line", "Line01", bus0 = "Bus0", bus1 = "Bus1", r = 1.21*0.02, x = 1.21*0.04,
             length = 1)
network.add("Line", "Line02", bus0 = "Bus0", bus1 = "Bus2", r = 1.21*0.01, x = 1.21*0.03,
             length = 1)
network.add("Line", "Line12", bus0 = "Bus1", bus1 = "Bus2", r = 1.21*0.0125, x = 1.21*0.025,
             length = 1)


# add loads to low voltage buses
network.add("Load", "Load01", bus = "Bus1", p_set = 256.6, q_set = 110.2)
network.add("Load", "Load02", bus = "Bus2", p_set = 138.6, q_set = 45.2)

# connect an external grid to HVB - Generator modelled as an external grid
network.add("Generator", "G1", bus = "Bus0", control = "Slack" )

network.pf()

# network.plot()
# plt.show()

