from numpy import *
from PIL import Image
import os

path =  "/Users/myazdaniUCSD/Documents/Ten_Thousand_Pairs/found_pairs_scratch/found_pairs_faceset/"

image_paths = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

image_sizes = [Image.open(image_path).size for image_path in image_paths]

xavg = 0
yavg = 0

for x,y in image_sizes:
  xavg += x
  yavg += y

print "average x", xavg/len(image_sizes)
print "average y", yavg/len(image_sizes)