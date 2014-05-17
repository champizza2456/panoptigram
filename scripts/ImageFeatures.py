from skimage.feature import hog
from HSV import *
from scipy.ndimage import filters

def grayScale_feature(img_name, image_size):
  return(array(Image.open(img_name).convert('L').resize(image_size)).flatten())

def HOG_feature(img_name, image_size):
  img_PIL = Image.open(img_name).resize(image_size)
  imgBW = array(img_PIL.convert('L'))	
  fd = hog(imgBW, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1))
  return fd[:,newaxis].flatten()

def Log_Sobel_feature(img_name, image_size):
  im = array(Image.open(img_name).resize(image_size).convert('L'))
  imx = zeros(im.shape)
  filters.sobel(im,1,imx)
  imy = zeros(im.shape)
  filters.sobel(im,0,imy)
  
  return log(sqrt(imx**2 + imy**2).flatten()+100)

def Sobel_feature(img_name, image_size):
  im = array(Image.open(img_name).resize(image_size).convert('L'))
  imx = zeros(im.shape)
  filters.sobel(im,1,imx)
  imy = zeros(im.shape)
  filters.sobel(im,0,imy)
  
  return sqrt(imx**2 + imy**2).flatten()

def H_feature(img_name, image_size):
  HSV = array(convert_my_hsv(Image.open(img_name).resize(image_size)))
  return HSV[0,:,:].flatten()
  
def S_feature(img_name, image_size):
  HSV = array(convert_my_hsv(Image.open(img_name).resize(image_size)))
  return HSV[1,:,:].flatten()

def V_feature(img_name, image_size):
  HSV = array(convert_my_hsv(Image.open(img_name).resize(image_size)))
  return HSV[2,:,:].flatten()
  
def HSV_feature(img_name, image_size):
  return array(convert_my_hsv(Image.open(img_name).resize(image_size)))[:,:,:].flatten()
 