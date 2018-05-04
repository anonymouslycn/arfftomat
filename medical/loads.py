import arff
import scipy.io as sio
import numpy as np
import codecs
file_ = codecs.open('medical.arff','r','UTF-8')
a = arff.load(file_)
c = a['data']
finalx = []
finaly = []
for i in range(len(c)):
	finalx.append(c[i][0:1449])
	finaly.append(c[i][1449:]) 
finalx=np.array(finalx)
finaly=np.array(finaly)
finalx=finalx.astype(float)
finaly=finaly.astype(float)
sio.savemat('medicalx.mat', {'x': finalx})  
sio.savemat('medicaly.mat', {'y': finaly})  
