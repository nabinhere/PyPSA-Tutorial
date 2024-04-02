import pypsa
import matplotlib.pyplot as plt
import numpy as np

n_bus = 3

network = pypsa.Network()

# add three buses in the network
# for i in range(n_bus):
#     network.add("Bus", f"Bus {i}", v_nom = 20.0)

network.add("Bus", "Bus 0", v_nom = 20.0, x=28.2096, y=83.9856)
network.add("Bus", "Bus 1", v_nom = 20.0, x=27.7172, y=85.3240)
network.add("Bus", "Bus 2", v_nom = 20.0, x=26.8065, y=87.2846)

# print bus details
print(network.buses, "\n\n")

# add lines between the buses
for i in range(n_bus):
    network.add("Line", f"Line {i}{(i+1)%3}", bus0 = f"Bus {i}", bus1 = f"Bus {(i+1)%n_bus}", x = 0.1, r = 0.01)

print(network.lines, "\n\n")

# add a generator at bus 0
network.add("Generator", "Generator 1", bus = "Bus 0", p_set = 100, control = "PQ")
print(network.generators.p_set, "\n\n")

network.add("Load", "Load 1", bus = "Bus 1", p_set = 100)
print(network.loads, "\n\n")
print(network.loads.p_set, "\n\n")

# perform the newton raphson load flow
network.pf()

# what is the active power flow in the lines?
print(network.lines_t.p0, "\n\n")

# ..and what are the voltage angle on the buses?
print(network.buses_t.v_ang*180/np.pi, "\n\n")

# print the magnitudes of bus voltages in per unit(pu)
print(network.buses_t.v_mag_pu, "\n\n")

network.export_to_csv_folder("53bus.csv")

