import EyePair
import os
src_path = "/Users/myazdaniUCSD/Documents/selfiecity/images/cities_20k/"
write_path = "/Users/myazdaniUCSD/Documents/Ten_Thousand_Pairs/found_pairs_cities/"
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
            

paths = get_immediate_subdirectories(src_path)

image_paths = [src_path + path for path in paths]

for image_path in image_paths:
  print image_path
  images = [os.path.join(image_path,f) for f in os.listdir(image_path) if f.endswith('.jpg')]
  for image in images:
    EyePair.return_eye_pair(image, write_path + image.split("/")[-1])
  