# Image compression using SVD
#
# Author: Sun Yan
# Date: 18/03/21
#
# This program has following dependencies:
# numpy, matplotlib, PIL
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = "Image\\Hin.jpg"
im = Image.open(path)
New_im = im.convert("L")
(W, H) = im.size

data = np.array(New_im)
im = Image.fromarray(data, mode="L")
New_im.save("Image\\oral.png",quality=100)


U,S,V  = np.linalg.svd(data,full_matrices=False)
print(np.shape(U),np.shape(S),np.shape(V),sep='\n\n')
Rnum = np.diag(S)
R = np.array(Rnum).shape[0]

res1 = np.dot(np.array(U), np.array(Rnum))
arr = np.dot(res1, np.array(V))
np.savetxt("Image\\result.txt", np.round(arr,2))


S = np.diag(Rnum)
print(S,U,V,sep='\n\n')
plt.plot(S, 'g^')
plt.title("Singular Value")
plt.ylabel("Size")
plt.xlabel("Position")
plt.show()
plt.savefig("Singular Value")
min_val = arr.min()
max_val = arr.max()
print(min_val,max_val,sep='\t')
#arr = (np.abs(arr)/(max_val-min_val))*255
arr[arr>255]=255
arr[arr<0]=0

im = Image.fromarray(np.uint8(arr), mode="L")

im.save("Image\\test.png",quality=100)

for i in range(1, R, 10):
    Rnum1 = np.array(Rnum)
    Rnum1[i:R, i:R] = 0
    compressratio = W * H / (i + i * (W + H));
    compressratio = np.round(compressratio,2)
    res1 = np.dot(np.array(U), Rnum1)
    arr = np.dot(res1, np.array(V))
    min_val = arr.min()
    max_val = arr.max()
   # arr = (np.abs(arr) / (max_val - min_val)) * 255
    arr[arr > 255] = 255
    arr[arr < 0] = 0
    im = Image.fromarray(np.uint8(arr), mode="L")
    im.save("Image\\" + str(i) + " " + str(compressratio) + ".png",quality=100)
    print("----------------------------->>>>" + str(i))


