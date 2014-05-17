import cv2
from numpy import *
import os

path = "/Users/myazdaniUCSD/Documents/Ten_Thousand_Pairs/found_pairs_source/"

write_path = '/Users/myazdaniUCSD/Documents/Ten_Thousand_Pairs/videos/'

image_paths = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]




codec = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')


#size = (int(img.shape[0]), int(img.shape[1]))
size = (184*5, 45*5)

#videoFile = cv2.VideoWriter();
#videoFile.open('MyOutputVid.mov', codec, 25, size,1)

fps = 7
videoWriter = cv2.VideoWriter(write_path+'EyePair_instagram_expanded_inter_lanczos4.mov', codec, fps, size, 1)

for image_path in image_paths:
  img =cv2.imread(image_path)
  resized = cv2.resize(img, size, interpolation = cv2.INTER_LANCZOS4)
  videoWriter.write(resized)

