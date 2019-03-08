import MDAnalysis
from MDAnalysis.analysis.waterdynamics import SurvivalProbability as SP
import numpy as np


u = MDAnalysis.Universe("md.gro", "md100ns.xtc", in_memory=True)
joined_sp_timeseries = [[] for _ in range(20)]
for lipid_id in range(1, 3 + 1):
    print("Lipid ID: %d" % lipid_id)

    selection = "resname POT and around 3.5 (resid %d and name O13 O14) " % lipid_id
    sp = SP(u, selection, verbose=False)
    sp.run(start=1, tau_max=20)

    # Raw SP points for each tau:
    for sps, new_sps in zip(joined_sp_timeseries, sp.sp_timeseries_data):
        sps.extend(new_sps)

# calculate the mean SP for each tau
sp_data = [np.mean(sp) for sp in joined_sp_timeseries]

for tau, sp in zip(range(1, 20 + 1), sp_data):
    print("{time} {sp}".format(time=tau, sp=sp))
