from PIL import Image
from matplotlib import pyplot
import numpy

img1 = numpy.array(Image.open('mergedImages/1.png').convert('L'))
img2 = numpy.array(Image.open('mergedImages/2.png').convert('L'))
img3 = numpy.array(Image.open('mergedImages/3.png').convert('L'))
img4 = numpy.array(Image.open('mergedImages/4.png').convert('L'))
img5 = numpy.array(Image.open('mergedImages/5.png').convert('L'))
img6 = numpy.array(Image.open('mergedImages/6.png').convert('L'))
img7 = numpy.array(Image.open('mergedImages/7.png').convert('L'))
img8 = numpy.array(Image.open('mergedImages/8.png').convert('L'))
img9 = numpy.array(Image.open('mergedImages/9.png').convert('L'))
img10 = numpy.array(Image.open('mergedImages/10.png').convert('L'))
img11 = numpy.array(Image.open('mergedImages/11.png').convert('L'))
img12 = numpy.array(Image.open('mergedImages/12.png').convert('L'))
img13 = numpy.array(Image.open('mergedImages/13.png').convert('L'))
img14 = numpy.array(Image.open('mergedImages/14.png').convert('L'))
img15 = numpy.array(Image.open('mergedImages/15.png').convert('L'))
img16 = numpy.array(Image.open('mergedImages/16.png').convert('L'))
img17 = numpy.array(Image.open('mergedImages/17.png').convert('L'))
img18 = numpy.array(Image.open('mergedImages/18.png').convert('L'))
img19 = numpy.array(Image.open('mergedImages/19.png').convert('L'))
img20 = numpy.array(Image.open('mergedImages/20.png').convert('L'))

out1 = numpy.empty([1080, 1920], dtype=int)
out2 = numpy.empty([1080, 1920], dtype=int)
out3 = numpy.empty([1080, 1920], dtype=int)
out4 = numpy.empty([1080, 1920], dtype=int)
out5 = numpy.empty([1080, 1920], dtype=int)
out6 = numpy.empty([1080, 1920], dtype=int)
out7 = numpy.empty([1080, 1920], dtype=int)
out8 = numpy.empty([1080, 1920], dtype=int)
out9 = numpy.empty([1080, 1920], dtype=int)
out10 = numpy.empty([1080, 1920], dtype=int)
out11 = numpy.empty([1080, 1920], dtype=int)
out12 = numpy.empty([1080, 1920], dtype=int)
out13 = numpy.empty([1080, 1920], dtype=int)
out14 = numpy.empty([1080, 1920], dtype=int)
out15 = numpy.empty([1080, 1920], dtype=int)
out16 = numpy.empty([1080, 1920], dtype=int)
out17 = numpy.empty([1080, 1920], dtype=int)
out18 = numpy.empty([1080, 1920], dtype=int)
out19 = numpy.empty([1080, 1920], dtype=int)
out20 = numpy.empty([1080, 1920], dtype=int)
out = numpy.empty([1080, 1920], dtype=int)

for j in range(1, 1919):
    for i in range(1, 1079):
        out1[i][j] = numpy.std([img1[i][j], img1[i - 1][j], img1[i][j - 1], img1[i + 1][j], img1[i][j + 1]])
        out2[i][j] = numpy.std([img2[i][j], img2[i - 1][j], img2[i][j - 1], img2[i + 1][j], img2[i][j + 1]])
        out3[i][j] = numpy.std([img3[i][j], img3[i - 1][j], img3[i][j - 1], img3[i + 1][j], img3[i][j + 1]])
        out4[i][j] = numpy.std([img4[i][j], img4[i - 1][j], img4[i][j - 1], img4[i + 1][j], img4[i][j + 1]])
        out5[i][j] = numpy.std([img5[i][j], img5[i - 1][j], img5[i][j - 1], img5[i + 1][j], img5[i][j + 1]])
        out6[i][j] = numpy.std([img6[i][j], img6[i - 1][j], img6[i][j - 1], img6[i + 1][j], img6[i][j + 1]])
        out7[i][j] = numpy.std([img7[i][j], img7[i - 1][j], img7[i][j - 1], img7[i + 1][j], img7[i][j + 1]])
        out8[i][j] = numpy.std([img8[i][j], img8[i - 1][j], img8[i][j - 1], img8[i + 1][j], img8[i][j + 1]])
        out9[i][j] = numpy.std([img9[i][j], img9[i - 1][j], img9[i][j - 1], img9[i + 1][j], img9[i][j + 1]])
        out10[i][j] = numpy.std([img10[i][j], img10[i - 1][j], img10[i][j - 1], img10[i + 1][j], img10[i][j + 1]])
        out11[i][j] = numpy.std([img11[i][j], img11[i - 1][j], img11[i][j - 1], img11[i + 1][j], img11[i][j + 1]])
        out12[i][j] = numpy.std([img12[i][j], img12[i - 1][j], img12[i][j - 1], img12[i + 1][j], img12[i][j + 1]])
        out13[i][j] = numpy.std([img13[i][j], img13[i - 1][j], img13[i][j - 1], img13[i + 1][j], img13[i][j + 1]])
        out14[i][j] = numpy.std([img14[i][j], img14[i - 1][j], img14[i][j - 1], img14[i + 1][j], img14[i][j + 1]])
        out15[i][j] = numpy.std([img15[i][j], img15[i - 1][j], img15[i][j - 1], img15[i + 1][j], img15[i][j + 1]])
        out16[i][j] = numpy.std([img16[i][j], img16[i - 1][j], img16[i][j - 1], img16[i + 1][j], img16[i][j + 1]])
        out17[i][j] = numpy.std([img17[i][j], img17[i - 1][j], img17[i][j - 1], img17[i + 1][j], img17[i][j + 1]])
        out18[i][j] = numpy.std([img18[i][j], img18[i - 1][j], img18[i][j - 1], img18[i + 1][j], img18[i][j + 1]])
        out19[i][j] = numpy.std([img19[i][j], img19[i - 1][j], img19[i][j - 1], img19[i + 1][j], img19[i][j + 1]])
        out20[i][j] = numpy.std([img20[i][j], img20[i - 1][j], img20[i][j - 1], img20[i + 1][j], img20[i][j + 1]])

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

result = Image.fromarray(out)
result.save('out.png')

# my_max = numpy.amax(out1)
# my_min = numpy.amin(out1)

# for j in range(1, 1919):
#     for i in range(1, 1079):
#         out1[i][j] = out1[i][j] * 255 / my_max

pyplot.imshow(out)
pyplot.gray()
pyplot.show()