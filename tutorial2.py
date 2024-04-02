import pypsa
import matplotlib.pyplot as plt

network = pypsa.Network()

nbus = 5

for i in range(nbus):
    network.add("Bus", f"Bus number {i}", v_nom = 132)

for i in range(nbus-1):
    network.add("Line", f"Line number {i}", bus0 = f"Bus number {i}", bus1 = f"Bus number {i+1}", r =0.02, x = 0.3)

network.add("Generator", "Slack Generator", bus = "Bus number 3", p_set = 60, control = "PV")

network.add("Load", "Load number 1", bus = "Bus number 4", p_set = 91, q_set = 41)

network.plot()

plt.show()

network.add()