import pypsa
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import cartopy.crs as ccrs

# %matplotlib inline
plt.rc("figure", figsize = (8,8))

network = pypsa.examples.ac_dc_meshed(from_master=True)
lines_current_type = network.lines.bus0.map(network.buses.carrier)
print(lines_current_type)

network.plot(
    line_colors=lines_current_type.map(lambda ct: "r" if ct == "DC" else "b"),
    title="Mixed AC (blue) - DC (red) network - DC (cyan)",
    color_geomap=True,
    jitter=0.3,
)

plt.tight_layout()

plt.show()

network.links.loc["Norwich Converter", "p_nom_extendable"] = False
