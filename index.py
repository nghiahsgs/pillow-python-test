#ref https://colab.research.google.com/drive/1raz-UHftq_ZuJ7g_wg8dBJy-aRL5ziMj#scrollTo=_9EwtcUfU2kI
#nguyenbanghia_T60@hus.edu.vn

from PIL import ImageFilter
from PIL import Image

#change file extension and save image
img1 = Image.open("bohetdi.jpg")
img1.save("bohetdi.png")

img1 = Image.open("bohetdi.jpg")
print(img1.size)
print(img1.format)
print(img1.mode)

#resize image
img1 = Image.open("bohetdi.jpg")
img1.thumbnail((100, 100))
img1.save("100.png")

#rotate image
img1 = Image.open("bohetdi.jpg")
img1 = img1.rotate(45)
img1

#convert gray scale
img1 = Image.open("bohetdi.jpg")
img1 = img1.convert(mode='L')
img1.save("gray.png")


#blur image
img1 = Image.open("bohetdi.jpg")
img1 = img1.filter(ImageFilter.GaussianBlur(15))
img1

#crop image
#toa do la goc tren cung ben trai, 0x la truc ngang, 0y doc xuong
img1 = Image.open("bohetdi.jpg")
area = (100, 500, 1150, 700)  # ((x1,y1),(x2,y2))
img1 = img1.crop(area)
img1

#combine image together
img1 = Image.open("bohetdi.png")
img2 = Image.open("bohetdi_text.png")
area = (0, 0, 1280, 960)
img1.paste(img2, area)
img1
# img=Image.merge('RGB',(img1,img2))
# img

#getting individual channel
img1 = Image.open("bohetdi.png")
r, g, b = img1.split()
r.mode
