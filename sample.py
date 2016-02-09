
#encoding:utf-8
import numpy as np
import copy
import matplotlib.pyplot as plt

fnew = np.zeros(100)
f = np.zeros(100)
#風上差分法
for i in range(0,100):
	if i < 50:
		f[i]=1.0
	else:
		f[i]=0.0 

#1次風上差分の計算	

MXK = 100
kai = 1.0
for kai in [0.0,0.25,0.5,0.75,1.0]:
	for k in range(0,MXK):
		for i in range(1,100):
			fnew[i]= f[i]-(f[i]-f[i-1])*kai #1次風上の計算
		for i in range(1,100):
			f[i]= fnew[i] #次ステップを計算
		f[0] = f[1]
		#print f[0],f[1],f[2],f[98],f[99]
		if ((k == 49) | (k == 99)):
			plt.xlabel("x")
			plt.ylabel("u")
			plt.title("upwind method_t:" + str(k) + "_c:" + str(kai))
			plt.plot(range(0,100),f,'.')
			filename = "upwind_t_" + str(k) + "_c_" + str(kai) +".png"
			plt.savefig(filename)
			plt.show()
			print "===1次風上差分法==="
			print ("uの出力 when t = " + str(k))
			print f


#ftcs
f = np.zeros(100)
fnew = np.zeros(100)
for i in range(0,100):
	if i < 50:
		f[i]=1.0
	else:
		f[i]=0.0

for k in range(0,1000): 
	for i in range(1,99):
		fnew[i] = (f[i] - kai/2.0 * (f[i+1] - f[i-1]))
	for i  in range(0,100):
		f[i] = fnew[i]
	f[0] = f[1]
	f[99] = f[98]
	if ((k == 49) | (k == 99)):
		plt.xlabel("x")
		plt.ylabel("u")
		plt.title("FTCS_Method_" + "c=1.0")
		plt.plot(range(0,100),f,'.')
		filename = "ftcs" + str(k) + ".png"
		plt.savefig(filename)
		plt.show()
		print "=======ftcs法===="
		print ("uの出力 when t = " + str(k))
		print f

#Lax-Friedrich法
f = np.zeros(100)
fnew = np.zeros(100)
for i in range(0,100):
	if i < 50:
		f[i]=1.0
	else:
		f[i]=0.0

for k in range(0,100): 
	for i in range(1,99):
		fnew[i] = ((f[i+1] + f[i-1])/2.0 - kai/2.0 * (f[i+1] - f[i-1]))
	for i  in range(0,100):
		f[i] = fnew[i]
	f[0] = f[1]
	f[99] = f[98]
	#print f[0],f[1],f[2],f[98],f[99]
	if ((k == 49) | (k == 99)):
		plt.xlabel("x")
		plt.ylabel("u")
		plt.title("LaxFriedrich_Method_" + "c=1.0")
		plt.plot(range(0,100),f,'.')
		filename = "Lax_Friedrich" + str(k) + ".png"
		plt.savefig(filename)
		plt.show()
		print "=====Lax_Friedrich法===="
		print ("uの出力 when t = " + str(k))
		print f

#LaxWendroff法
f = np.zeros(100)
fnew = np.zeros(100)
for i in range(0,100):
	if i < 50:
		f[i]=1.0
	else:
		f[i]=0.0

for kai in [0.0,0.25,0.5,0.75,1.0]:
	for k in range(0,100): 
		for i in range(1,99):
			fnew[i] = (f[i] - kai/2.0 * (f[i+1] - f[i-1]) + kai * kai/2.0 * (f[i+1] - 2 * f[i] + f[i-1]))
		for i  in range(0,100):
			f[i] = fnew[i]
		f[0] = f[1]
		f[99] = f[98]
		#print f[0],f[1],f[2],f[98],f[99]
		if ((k == 49) | (k == 99)):
			plt.xlabel("x")
			plt.ylabel("u")
			plt.title("LaxWendroff_t:" + str(k) + "_c:" + str(kai))
			plt.plot(range(0,100),f,'.')
			filename = ("LaxWendroff" + "_t_" + str(k) + "c_" + str(kai) + ".png")
			plt.savefig(filename)
			plt.show()
			print "=====LaxWendroff法===="
			print ("uの出力 when t = " + str(k))
			print f
