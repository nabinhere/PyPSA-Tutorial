import pypsa
import pandas as pd
import matplotlib.pyplot as plt

network = pypsa.Network()

# add high voltage bus
network.add("Bus", "HVB", v_nom = 11.0)

# add low voltage buses
for i in range(1,4):
    network.add("Bus", f"LVB0{i}", v_nom = 0.4)

# add distribution lines between the low voltage buses
network.add("Line", "Line12", bus0 = "LVB01", bus1 = "LVB02", r = 0.082*0.3, x = 0.7*0.3,
             length = 0.3)
network.add("Line", "Line13", bus0 = "LVB01", bus1 = "LVB03", r = 0.082*0.4, x = 0.7*0.4, 
            length = 0.4)

# add a transformer between HVB and LVB01
network.add("Transformer", "T", bus0 = "HVB", bus1 = "LVB01", model = "t", s_nom = 0.25,
            r = 0.5, x = 0.8)


# add loads to low voltage buses
network.add("Load", "Load02", bus = "LVB02", p_set = 0.01, q_set = 0.004)
network.add("Load", "Load03", bus = "LVB03", p_set = 0.01, q_set = 0.005)

# connect an external grid to HVB - Generator modelled as an external grid
network.add("Generator", "External Grid", bus = "HVB", control = "Slack" )

network.pf()

# network.plot()
# plt.show()

