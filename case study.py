import pypsa
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

network = pypsa.Network()

# add high voltage bus
network.add("Bus", "bus01", v_nom = 0.4)
network.add("Generator", "G01", bus = "bus01", p_set = 0.020)
network.add("Load", "L01", bus = "bus01", p_set = 0.012, q_set = 0.008)

network.pf()



