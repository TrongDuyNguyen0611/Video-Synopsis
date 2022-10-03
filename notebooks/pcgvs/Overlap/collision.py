import cv2
import glob
import numpy as np
import os
from PIL import Image
from os import path, getcwd


# overlay = cv2.imread('/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/patches/44.jpg')
# background = cv2.imread('/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/background.jpg')
# rows,cols,channels = overlay.shape  

# f = open("/Users/nguyenduy/Desktop/pcgvs-main/notebooks/data/a.txt", "r")
# string = f.read()
# list = string.split(", ")
# f.close()

path="/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/patches"
images = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.jpg']

# reList = []
# imList=[]
# overlist=[]

# for i in images:
#     reList.append(i.split("_")[1][0:-4])
# for i in reList:
#     imList.append(i[0:-4])
# for i in list:  
#     if i in imList:
#         overlist.append(i)

# for i in images:
#     if i.split("_")[1][0:-4] in list:
#         overlay = cv2.imread('/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/patches/'+str(i))
#         background = cv2.imread('/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/patches/'+str(i))
#         rows,cols,channels = overlay.shape  
#         overlay=cv2.addWeighted(background[0:rows, 0:cols],0.5,overlay,0.5,0)
#         background[0:rows, 0:cols ] = overlay
#         cv2.imwrite('/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/patches/'+str(i),overlay)
#         print(i)



# im = cv2.imread("/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/patches/10_527.jpg")
# bg= cv2.imread("/Users/nguyenduy/Desktop/pcgvs-main/notebooks/synopsis/background.jpg")

# # Create an all white mask
# mask = 255 * np.ones(im.shape, im.dtype)

# # The location of the center of the src in the dst
# width, height, channels = im.shape
# center = (height//2, width//2)

# # Seamlessly clone src into dst and put the results in output
# normal_clone = cv2.seamlessClone(im, bg, mask, center, cv2.NORMAL_CLONE)
# # mixed_clone = cv2.seamlessClone(bg, im, mask, center, cv2.MIXED_CLONE)

# # Write results
# cv2.imwrite("/Users/nguyenduy/Desktop/pcgvs-main/notebooks/data/1.jpg", normal_clone)





