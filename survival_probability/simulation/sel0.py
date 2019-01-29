import MDAnalysis
from MDAnalysis.analysis.waterdynamics import SurvivalProbability as SP
import matplotlib.pyplot as plt

u = MDAnalysis.Universe("md.gro", "md.xtc")
selection = "resname POT and around 3.35 (resname DOPC and name O13 O14) "

found0_counter = 0
found_counter = 0
for ts in u.trajectory[::10]:
	print (ts.time / 1000.0)
	selected = u.select_atoms(selection)
	if len(selected) == 0:
		found0_counter += 1
		print ('yeayeayea')
	else:
		found_counter += 1

print ('found 0', found0_counter)
print ('found', found_counter)