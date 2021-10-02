import numpy as np
from PIL import Image

#reading the image, can be changed to any file on your system.
image = Image.open("Image\Masked\Example 1 zoomed #2- maasked.png")
data = np.asarray(image)

#the code below can be uncommented to find the number of pixles in colums and rows
#print(data.shape)

#use y and x if you want the entire picture to be evaluated
#y = data.shape[0]
#x = data.shape[1]

#this can be used to crop a section of an masked image and find the percentage of vegetation in that croped section. 10,10 is just a place holder and can be changed
section = [(0,0), (10,10)]

#this is used to find the size of the croped section
size = (abs(section[0][0]- section[1][0]), abs(section[0][1] - section[1][1]))

#this will be used for the loop, where to start counting
startx = section[0][1]
starty = section[0][0]

#this finds how many pixles are in the section 
pxsize = size[0] * size[1]

#this counts how many pixels are populated with color, which means vegetation
count = 0
for i in range(size[0]):
    for j in range(size[1]):
        px = data[i+startx][j+starty]
        if px[1] != 0:
            count += 1

#this finds the percentage and rounds it to 2 decimal place
percentage = round(count/pxsize *100, 2)

if (percentage > 30):
    print("Roads are not recommended because this area is likely a forest or park.")
elif (percentage < 15):
    print("Roads are not recommended because this area is likely aresidential area.")
else:
    print("Roads can be build here.")

print (percentage)