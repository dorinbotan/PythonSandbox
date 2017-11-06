from PIL import Image
from matplotlib import pyplot
import numpy

img1 = numpy.array(Image.open('images/1.png').convert('L'))
img2 = numpy.array(Image.open('images/2.png').convert('L'))
img3 = numpy.array(Image.open('images/3.png').convert('L'))
img4 = numpy.array(Image.open('images/4.png').convert('L'))
img5 = numpy.array(Image.open('images/5.png').convert('L'))
img6 = numpy.array(Image.open('images/6.png').convert('L'))
img7 = numpy.array(Image.open('images/7.png').convert('L'))
img8 = numpy.array(Image.open('images/8.png').convert('L'))
img9 = numpy.array(Image.open('images/9.png').convert('L'))
img10 = numpy.array(Image.open('images/10.png').convert('L'))
img11 = numpy.array(Image.open('images/11.png').convert('L'))
img12 = numpy.array(Image.open('images/12.png').convert('L'))
img13 = numpy.array(Image.open('images/13.png').convert('L'))
img14 = numpy.array(Image.open('images/14.png').convert('L'))
img15 = numpy.array(Image.open('images/15.png').convert('L'))
img16 = numpy.array(Image.open('images/16.png').convert('L'))
img17 = numpy.array(Image.open('images/17.png').convert('L'))
img18 = numpy.array(Image.open('images/18.png').convert('L'))
img19 = numpy.array(Image.open('images/19.png').convert('L'))
img20 = numpy.array(Image.open('images/20.png').convert('L'))

# out1 = numpy.convolve(img1, [])

import scipy.signal as sg
from scipy import ndimage

M, N, P = 4, 10, 20

# kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
# kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
# kernel = [[1, 2, 3, 4, 5, 1, 5, 4, 3, 2, 1]]
# kernel = [[3, 10, 3], [0, 0, 0], [-3, -10, -3]]
# kernel1 = [[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]]

# out = sg.convolve(kernel, img1, 'full')

print(1)

out1 = ndimage.sobel(img1)
out2 = ndimage.sobel(img2)
out3 = ndimage.sobel(img3)
out4 = ndimage.sobel(img4)
out5 = ndimage.sobel(img5)
out6 = ndimage.sobel(img6)
out7 = ndimage.sobel(img7)
out8 = ndimage.sobel(img8)
out9 = ndimage.sobel(img9)
out10 = ndimage.sobel(img10)
out11 = ndimage.sobel(img11)
out12 = ndimage.sobel(img12)
out13 = ndimage.sobel(img13)
out14 = ndimage.sobel(img14)
out15 = ndimage.sobel(img15)
out16 = ndimage.sobel(img16)
out17 = ndimage.sobel(img17)
out18 = ndimage.sobel(img18)
out19 = ndimage.sobel(img19)
out20 = ndimage.sobel(img20)

out = numpy.empty([1080, 1920], dtype=int)

for j in range(1, 1919):
    for i in range(1, 1079):
        maximum = max(out1[i][j], out2[i][j], out3[i][j], out4[i][j], out5[i][j],
                      out6[i][j], out7[i][j], out8[i][j], out9[i][j], out10[i][j],
                      out11[i][j], out12[i][j], out13[i][j], out14[i][j], out15[i][j],
                      out16[i][j], out17[i][j], out18[i][j], out19[i][j], out20[i][j])

        if maximum == out1[i][j]:
            out[i][j] = 22
        elif maximum == out2[i][j]:
            out[i][j] = 34
        elif maximum == out3[i][j]:
            out[i][j] = 46
        elif maximum == out4[i][j]:
            out[i][j] = 58
        elif maximum == out5[i][j]:
            out[i][j] = 70
        elif maximum == out6[i][j]:
            out[i][j] = 82
        elif maximum == out7[i][j]:
            out[i][j] = 94
        elif maximum == out8[i][j]:
            out[i][j] = 106
        elif maximum == out9[i][j]:
            out[i][j] = 118
        elif maximum == out10[i][j]:
            out[i][j] = 130
        elif maximum == out11[i][j]:
            out[i][j] = 142
        elif maximum == out12[i][j]:
            out[i][j] = 154
        elif maximum == out13[i][j]:
            out[i][j] = 166
        elif maximum == out14[i][j]:
            out[i][j] = 178
        elif maximum == out15[i][j]:
            out[i][j] = 190
        elif maximum == out16[i][j]:
            out[i][j] = 202
        elif maximum == out17[i][j]:
            out[i][j] = 214
        elif maximum == out18[i][j]:
            out[i][j] = 226
        elif maximum == out19[i][j]:
            out[i][j] = 238
        elif maximum == out20[i][j]:
            out[i][j] = 250

    print(j * 100 / 1920)
print(100)

pyplot.imshow(out1)
pyplot.gray()
pyplot.show()
pyplot.imshow(out)
pyplot.gray()
pyplot.show()