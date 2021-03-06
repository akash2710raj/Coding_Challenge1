from cv2 import cv2
import numpy as np

# load image and get dimensions
path = "D:/Coding_Challenge1/Computer Vision/Task-1b.png"
img = cv2.imread(path,0)
resize_img = cv2.resize(img,(600,500))
h, w = resize_img.shape

# create zeros mask 2 pixels larger in each dimension
mask = np.zeros([h + 2, w + 2], np.uint8)
print(mask.shape)

# do floodfill
result = resize_img.copy()

#Right Hand Side
cv2.floodFill(result, mask, (0,0), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (0,250), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (0,300), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (0,450), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (90,300), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (85,280), (255,255,255), (3,151,65), (3,151,65), flags=8)

#Left Hand Side
cv2.floodFill(result, mask, (590,0), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (580,240), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (580,250), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (555,255), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (560,260), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (595,280), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (595,290), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (570,290), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (590,340), (255,255,255), (3,151,65), (3,151,65), flags=8)

#Down Side
cv2.floodFill(result, mask, (550,480), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (250,480), (255,255,255), (3,151,65), (3,151,65), flags=8)

#Up Side
cv2.floodFill(result, mask, (130,0), (255,255,255), (3,151,65), (3,151,65), flags=8)



cv2.floodFill(result, mask, (130,130), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (128,130), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (136,132), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (132,160), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (160,160), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (135,162), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (135,164), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (137,163), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (133,200), (255,255,255), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (133,290), (255,255,255), (3,151,65), (3,151,65), flags=8)


#& o
# cv2.floodFill(result, mask, (250,80), (255,255,255), (3,151,65), (3,151,65), flags=8)


# 


# write result to disk
cv2.imwrite("Final_image.jpg", result)

# display it
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()