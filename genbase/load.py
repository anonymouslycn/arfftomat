from scipy.io import arff
import scipy.io as sio
from io import StringIO
import numpy as np
f = open("genbase.arff")
f = f.read()
f = StringIO(f)
data, meta = arff.loadarff(f)


final = []
for i in range(len(data)):
	now = []
	for j in range(1,1186):
		# print (data[i][j])
		if data[i][j]==b'NO':
			# print ("ok")
			now.append(0)
		else:
			now.append(1)
	final.append(now)
final=np.array(final)
final=final.astype(float)
sio.savemat('genbasex.mat', {'x': final})  

final = []
for i in range(len(data)):
	now = []
	for j in range((1186),len(data[0])):
		now.append(data[i][j])
	final.append(now)
final=np.array(final)
final=final.astype(float)
sio.savemat('genbasey.mat', {'y': final})  