import cv2
import numpy as np
image = cv2.imread('memahahaha.jpg')

# Отображение изображения 
""""
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
"""
resized_image = cv2.resize(image, (500, 500))

print("Высота:"+str(image.shape[0]))

print("Ширина:" + str(image.shape[1]))

print("Количество каналов:" + str(image.shape[2]))
""""
cv2.rectangle(image, (50, 50), (50 + 10, 60 + 10), (255, 0, 0), 5)

cv2.imshow('Image1', image) 
cv2.waitKey(0)
"""
x = np.uint8([250])
y = np.uint8([10])
 
print( cv2.add(x,y) ) # 250+10 = 260 => 255
[[255]]
 
print( x+y )          # 250+10 = 260 % 256 = 4
[4]