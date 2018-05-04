from scipy.io import arff
import scipy.io as sio
from io import StringIO
import numpy as np
f = open("CAL500.arff")
f = f.read()
f = StringIO(f)
data, meta = arff.loadarff(f)


final = []
for i in range(len(data)):
	now = []
	for j in range(242-174):
		now.append(data[i][j])
	final.append(now)
final=np.array(final)
final=final.astype(float)
sio.savemat('CAL500x.mat', {'x': final})  

final = []
for i in range(len(data)):
	now = []
	for j in range((242-174),len(data[0])):
		now.append(data[i][j])
	final.append(now)
final=np.array(final)
final=final.astype(float)
sio.savemat('CAL500y.mat', {'y': final})  