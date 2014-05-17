from PIL import Image
from pylab import *

def convert_my_hsv(imgPIL):
	i = imgPIL.convert('RGB')
	a = array(i, int)
	R = a[:,:,0]
	G = a[:,:,1]
	B = a[:,:,2]
	
	m = a.min(2)
	M = a.max(2)
	
	C = M-m
	Cmsk = C!=0
	
	H = zeros(R.shape, int)
	mask = (M==R)&Cmsk
	H[mask] = mod(60*(G-B)/C, 360)[mask]
	mask = (M==G)&Cmsk
	H[mask] = (60*(B-R)/C + 120)[mask]
	mask = (M==B)&Cmsk
	H[mask] = (60*(R-G)/C + 240)[mask]
	H *= 255
	H /= 360 # if you prefer, leave as 0-360, but don't convert to uint8
	
	# Value
	V = M
	
	# Saturation
	S = zeros(R.shape, int)
	S[Cmsk] = ((255*C)/V)[Cmsk]
	
	# H, S, and V are now defined as integers 0-255
	return H, S, V
	
