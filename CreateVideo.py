import os
from tkinter import Frame
import cv2

path ="Images/"
Images = []
for file in os.listdir(path):
    name,ext= os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpeg', '.jfif', '.jpg']:
        file_name = path+"/"+file
        print(file_name)
        Images.append(file_name)

count=len(Images)
print(len(Images))

frame=cv2.imread(Images[0])

height, width, Channels = frame.shape

size = (width,height)
print(size)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count):
    print(Images[i])
    frame=cv2.imread(Images[i])
    out.write(frame)

out.release()
print("Done")