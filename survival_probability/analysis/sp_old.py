import MDAnalysis
from MDAnalysis.analysis.waterdynamics import SurvivalProbability as SP
import numpy as np

u = MDAnalysis.Universe("md.gro", "md100ns.xtc", in_memory=True)

sp_lists = [[] for _ in range(20)]
for lipid_id in range(1, 100 + 1):
    print("Lipid ID", lipid_id)
    selection = "resname POT and around 3.5 (resid %d and name O13 O14) " % lipid_id
    sp = SP(u, selection, t0=0, tf=10000, dtmax=20)
    sp.run()

    for tau_list, new_tau in zip(sp_lists, sp.timeseries):
        tau_list.append(new_tau)

sp_data = [np.mean(sp) for sp in sp_lists]
for tau, sp in zip(range(1, 20 + 1), sp_data):
    print("{time} {sp}".format(time=tau, sp=sp))