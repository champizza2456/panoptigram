import os
import operator
from my_montage_maker import *
import math
from PIL import Image
import random

src_path = "/Users/myazdaniUCSD/Documents/Ten_Thousand_Pairs/found_pairs_scratch/found_pairs_faceset/"
montage_path = "../montages/"


nrows = 202 #71
ncols = 43 #30
#image_dim = 30
total_images = nrows*ncols
photow = 71 #184
photoh = 17 #45
photo = (photow,photoh)
margins = [0,0,0,0]
padding = 0

image_paths = [os.path.join(src_path,f) for f in os.listdir(src_path) if f.endswith('.jpg')]
#if len(image_path) < total_images: continue

##randomization
#inds = random.sample(range(len(image_list)), total_images)
#image_list = [image_list[i] for i in inds]

inew = make_contact_sheet(image_paths,(ncols,nrows),photo,margins,padding)
inew.save(montage_path+"faceset_eyes.jpg")

	