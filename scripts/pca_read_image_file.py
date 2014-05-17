import os
from PIL import Image, ImageDraw
from numpy import *
from pylab import *
import pickle
import csv
import pca
from scipy.cluster.vq import *
import ImageFeatures


outpath = "../pca_vis/instagram_pc_2_3_"
#outfile = "france_HOG_feature.jpg"
src_path = "../images/instagram/"


image_list = [os.path.join(src_path,f) for f in os.listdir(src_path) if f.endswith('.jpg')]

image_size = (200,200)


def generate_PCA_viz(feature_matrix, file_name):
  V,S,immean = pca.pca(feature_matrix)
  projected_features = array([dot(V[[1,2]],feature_matrix[i]-immean) for i in range(len(image_list))])
  
  #h,w = 10000,10000
  h,w = 25000,25000
  img = Image.new('RGB',(w,h),(255,255,255))
  draw = ImageDraw.Draw(img)

  scale = abs(projected_features).max(0)
  scaled = floor(array([ (p / scale) * (w/2-20,h/2-20) + (w/2,h/2) for p in projected_features]))
  for i in range(len(image_list)):
    nodeim = Image.open(image_list[i]) 
    nodeim = nodeim.resize((375,375))
    #nodeim = nodeim.resize(image_size)
    ns = nodeim.size 
    img.paste(nodeim,(int(scaled[i][0]-ns[0]//2),int(scaled[i][1]-ns[1]//2),int(scaled[i][0]+ns[0]//2+1),int(scaled[i][1]+ns[1]//2+1))) 
	
  img.save(file_name)
  

immatrix = array([ImageFeatures.HOG_feature(im, image_size) for im in image_list], 'f')
generate_PCA_viz(immatrix, outpath +"HOG.jpg")

immatrix = array([ImageFeatures.grayScale_feature(im, image_size) for im in image_list], 'f')
generate_PCA_viz(immatrix, outpath +"GrayScale.jpg")

immatrix = array([ImageFeatures.Log_Sobel_feature(im, image_size) for im in image_list], 'f')
generate_PCA_viz(immatrix, outpath +"LogSobel.jpg")

immatrix = array([ImageFeatures.Sobel_feature(im, image_size) for im in image_list], 'f')
generate_PCA_viz(immatrix, outpath +"Sobel.jpg")