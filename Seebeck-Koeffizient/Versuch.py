import numpy as np
import glob
import metrolopy as uc

musterT302 = 'T302/*UMessung.txt'

dateienT302 = glob.glob(musterT302)

for path in dateienT302:
    with open(path, 'r') as f:
        lines = f.readlines()
        Messwerte = np.array(lines[1].split(), dtype=float)
        Messwert = uc.gummy(np.mean(Messwerte),u=np.std(Messwerte), unit='Ohm')


print(Messwerte)
