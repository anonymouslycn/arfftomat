import arff
import scipy.io as sio
import numpy as np
import codecs
file_ = codecs.open('delicious.arff','r','UTF-8')
a = arff.load(file_)
c = a['data']
finalx = []
finaly = []
for i in range(len(c)):
	finalx.append(c[i][0:500])
	finaly.append(c[i][500:]) 
finalx=np.array(finalx)
finaly=np.array(finaly)
finalx=finalx.astype(float)
finaly=finaly.astype(float)
sio.savemat('deliciousx.mat', {'x': finalx})  
sio.savemat('deliciousy.mat', {'y': finaly})  
