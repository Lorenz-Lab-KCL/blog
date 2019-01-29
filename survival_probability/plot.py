import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({'font.size': 12})

# Transform for easier graphing
old_sp = np.loadtxt("old_sp.txt").T
new_sp = np.loadtxt("new_sp.txt").T

plt.title('SP of K around O')
plt.plot(old_sp[0], old_sp[1], label='T0 bug SP')
plt.plot(new_sp[0], new_sp[1], label='Corrected SP')
plt.xlabel('$Tau$')
plt.ylabel('SP')
plt.ylim([0, 1])
plt.xticks(range(1,20 + 1))

plt.legend()
plt.savefig('t0_bug.png', dpi=300)
#plt.show()