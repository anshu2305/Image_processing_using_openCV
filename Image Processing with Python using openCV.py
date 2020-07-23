#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2
import numpy as np

def sharpen(image):
    #got these values from GIMP 
    kernel=np.array([[0,-1,0], [-1,5,-1],[0,-1,0]])
    #filters2D accepts 3 arguments src, depth, kernel
    sharpen_img= cv2.filter2D(image,-1,kernel)
    cv2.imshow("Sharpened Image",sharpen_img)
    cv2.waitKey(0)
    return sharpen_img

def blur(image):
    kernel_sizes=[3,5,9,13]
    for i,k in enumerate(kernel_sizes):
        blur_img= cv2.blur(image, ksize=(k,k))
        cv2.imshow(str(k),blur_img)
        cv2.waitKey(0)
    return    
        

def resize(fname, width, height):
    img= cv2.imread(fname)
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    org_h,org_w= img.shape[0:2]
    print("height", org_h)
    print("width", org_w)
    
    if (org_w >= org_h):
        new_img=cv2.resize(img, (width,height))
    else:
        new_img=cv2.resize(img, (height,width))
    return fname, new_img
file=input("Enter the path of image to be processed: ")
filename, new_img = resize(file,540,440)
cv2.imshow("Resized image", new_img)
cv2.waitKey(0)
blur(new_img) #shows blur effect for different values of kernel
sharpen(new_img)


# In[ ]:





# In[ ]:




